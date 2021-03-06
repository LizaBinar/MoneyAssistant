"""Second_day

Revision ID: ca75369de92c
Revises: 
Create Date: 2022-06-02 16:06:48.022870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca75369de92c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.Text(length=55), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('balans', sa.Float(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('category', sa.Text(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transactions_id'), 'transactions', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transactions_id'), table_name='transactions')
    op.drop_table('transactions')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
