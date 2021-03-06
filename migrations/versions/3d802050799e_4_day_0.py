"""4_day.0

Revision ID: 3d802050799e
Revises: 3509de210676
Create Date: 2022-06-09 17:59:59.688653

"""
import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d802050799e'
down_revision = '3509de210676'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('plus_or_minus', sa.Boolean(), nullable=True),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('category', sa.Text(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transactions_id'), 'transactions', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transactions_id'), table_name='transactions')
    op.drop_table('transactions')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
