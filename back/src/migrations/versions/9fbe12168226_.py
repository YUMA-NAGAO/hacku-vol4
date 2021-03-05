"""empty message

Revision ID: 9fbe12168226
Revises: 1e13dfec183c
Create Date: 2021-03-05 01:52:51.936763

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9fbe12168226'
down_revision = '1e13dfec183c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('picture_url', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('status_message', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'status_message')
    op.drop_column('users', 'picture_url')
    # ### end Alembic commands ###