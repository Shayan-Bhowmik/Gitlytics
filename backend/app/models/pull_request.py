import uuid
from datetime import datetime 
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.sql import func
from app.models.base import Base

class PullRequest(Base):
    __tablename__ = "pull_requests"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    repo_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id", ondelete="CASCADE"))
    github_pr_id: Mapped[int] = mapped_column(Integer, unique=True)
    title: Mapped[str] = mapped_column(String(255))
    author_github_id: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    merged_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    review_delay_minutes: Mapped[int | None] = mapped_column(Integer)