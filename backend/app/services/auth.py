import httpx 
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.config import settings


async def exchange_code_for_token(code:str)->str | None:

    """Sends the temporary code to GitHub to get an access token.
    GitHub API endpoint: https://github.com/login/oauth/access_token
    """
    async with httpx.AsyncClient() as client:
        response=await client.post(
            "https://github.com/login/oauth/access_token",
            json={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={
                "Accept": "application/json"
            },
        )
        data=response.json()
        return data.get("access_token")


async def fetch_github_user(access_token: str)->dict|None:
    
    """Uses the access token to fetch the user's GitHub profile
    Github API endpoint: https:api.github.com/user
    """
    async with httpx.AsyncClient() as client:
        response=await client.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
            }
        )
        if response.status_code == 200:
            return response.json()
        return None
    


async def upsert_user(db: AsyncSession, github_user: dict, access_token: str)->User:

    """Creates a new user or updates an existing one based on their github id"""
    
    result=await db.execute(
        select(User).where(User.github_id == github_user["id"])
    )
    user=result.scalar_one_or_none()

    if user:
        user.username=github_user["login"]
        user.email=github_user.get("email", "")
        user.avatar_url=github_user.get("avatar_url")
        user.access_token=access_token
    else:
        user=User(
            github_id=github_user["id"],
            username=github_user["login"],
            email=github_user.get("email", ""),
            avatar_url=github_user.get("avatar_url"),
            access_token=access_token,
        )
        db.add(user)
    
    await db.commit()
    await db.refresh(user)
    return user