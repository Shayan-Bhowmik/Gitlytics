"""enable_analytics_rls

Revision ID: cd05d0380576
Revises: 17a3f812c3c6
Create Date: 2026-06-24 00:30:22.017044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd05d0380576'
down_revision: Union[str, Sequence[str], None] = '17a3f812c3c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TABLE analytics ENABLE ROW LEVEL SECURITY;")


def downgrade() -> None:
    """Downgrade schema."""
    pass
