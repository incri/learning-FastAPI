"""adding adress id on user table to create relationship between user and address

Revision ID: 1d715894931c
Revises: 7f4611e80889
Create Date: 2023-07-27 11:54:05.595500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1d715894931c"
down_revision = "7f4611e80889"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "address_users_fk",
        source_table="users",
        referent_table="address",
        local_cols=["address_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
