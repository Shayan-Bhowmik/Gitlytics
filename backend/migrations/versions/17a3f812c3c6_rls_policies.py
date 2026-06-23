"""rls_policies

Revision ID: 17a3f812c3c6
Revises: 274b52bd0c4e
Create Date: 2026-06-24 00:14:17.884033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17a3f812c3c6'
down_revision: Union[str, Sequence[str], None] = '274b52bd0c4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TABLE users ENABLE ROW LEVEL SECURITY;")
    op.execute("ALTER TABLE repositories ENABLE ROW LEVEL SECURITY")
    op.execute("""CREATE POLICY 
        "Users can manage their own record"
        ON users FOR ALL USING (auth.uid() = id);       
    """)

    op.execute("""
        CREATE POLICY 
        "User can manage their own repositories"
        ON repositories FOR ALL USING (auth.uid() = owner_id);
    """)

    op.execute("""
        CREATE POLICY 
        "Users can view analytics for their repos"
        ON analytics FOR SELECT USING (
            EXISTS(
                SELECT 1 FROM repositories 
                WHERE repositories.id = analytics.repo_id
                AND
                repositories.owner_id = auth.uid()
            )
        );
    """)



def downgrade() -> None:
    """Downgrade schema."""
    pass
