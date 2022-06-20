""" creates known error version table

Revision ID: 6d1ea3d02057
Revises: 08f15edbcdb6
Create Date: 2022-06-18 21:02:00.483887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d1ea3d02057'
down_revision = '08f15edbcdb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('known_error_version',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('solution', sa.String(length=1000), nullable=False),
    sa.Column('version_number', sa.SmallInteger(), nullable=False),
    sa.Column('known_error_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['known_error_id'], ['known_error.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('known_error', sa.Column('current_version_id', sa.Integer(), nullable=True))
    op.create_foreign_key('error_current_version_id', 'known_error', 'known_error_version', ['current_version_id'], ['id'])
    op.drop_column('known_error', 'solution')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('known_error', sa.Column('solution', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    # op.drop_constraint('error_current_version_id', 'known_error', type_='foreignkey')
    op.drop_column('known_error', 'current_version_id')
    op.drop_table('known_error_version')
    # ### end Alembic commands ###