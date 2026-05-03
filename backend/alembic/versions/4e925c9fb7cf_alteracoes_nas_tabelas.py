"""Alteracoes nas tabelas

Revision ID: 4e925c9fb7cf
Revises: 9891fcfec25a
Create Date: 2026-05-02 23:39:59.082500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '4e925c9fb7cf'
down_revision: Union[str, Sequence[str], None] = '9891fcfec25a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    op.drop_constraint(op.f('equipaments_client_id_fkey'), 'equipaments', type_='foreignkey')
    op.drop_column('equipaments', 'client_id')
    
    op.add_column('equipaments', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'equipaments', 'users', ['user_id'], ['id'])
    
    op.drop_index(op.f('ix_clients_email'), table_name='clients')
    op.drop_table('clients')


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table('clients',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('telephone', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('clients_pkey'))
    )
    op.create_index(op.f('ix_clients_email'), 'clients', ['email'], unique=True)
    
    op.drop_constraint(None, 'equipaments', type_='foreignkey')
    op.drop_column('equipaments', 'user_id')
    
    op.add_column('equipaments', sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key(op.f('equipaments_client_id_fkey'), 'equipaments', 'clients', ['client_id'], ['id'])
    
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')