"""Renaming students to scholars

Revision ID: 1d0d3f35a89c
Revises: 
Create Date: 2025-03-08 21:47:49.272568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d0d3f35a89c'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.rename_table('students', 'scholars')

def downgrade():
    op.rename_table('scholars', 'students')
