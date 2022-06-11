""" Added Known Error Table

Revision ID: c63103106c73
Revises: 9d5d10759e36
Create Date: 2022-06-11 13:48:48.876421

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c63103106c73'
down_revision = '9d5d10759e36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('known_error',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('priority', sa.String(length=20), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_blocked', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('taken_by', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.username'], ),
    sa.ForeignKeyConstraint(['taken_by'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('incident_known_error',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('known_error_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['incident.id'], ),
    sa.ForeignKeyConstraint(['known_error_id'], ['known_error.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('know_error')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('know_error',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('priority', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_blocked', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('taken_by', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.username'], name='know_error_created_by_fkey'),
    sa.ForeignKeyConstraint(['taken_by'], ['user.username'], name='know_error_taken_by_fkey'),
    sa.PrimaryKeyConstraint('id', name='know_error_pkey')
    )
    op.drop_table('incident_known_error')
    op.drop_table('known_error')
    # ### end Alembic commands ###
