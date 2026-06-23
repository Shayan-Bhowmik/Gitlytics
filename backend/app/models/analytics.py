from sqlalchemy.dialects.postgresql import JSONB
import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.sql import func
from app.models.base import Base

class Analytics(Base):
    __tablename__ = "analytics"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    repo_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id", ondelete="CASCADE"))
    week_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    commit_count: Mapped[int] = mapped_column(Integer)
    pr_merge_time_avg: Mapped[int] = mapped_column(Integer)
    issue_resolution_avg: Mapped[int] = mapped_column(Integer)
    health_score: Mapped[int] = mapped_column(Integer)
    computed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())