from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str
    JWT_SECRET_KEY: str
    OPENAI_API_KEY: str
    NEXT_PUBLIC_API_URL: str

    model_config = SettingsConfigDict(env_file=(".env", "../.env"))


settings = Settings()