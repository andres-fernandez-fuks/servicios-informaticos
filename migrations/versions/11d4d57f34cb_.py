"""empty message

Revision ID: 11d4d57f34cb
Revises: 06ec911210f1
Create Date: 2022-04-28 19:25:13.030505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11d4d57f34cb'
down_revision = '06ec911210f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('permissions', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('is_enabled', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_visible', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('entity', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('lastname', sa.String(length=60), nullable=True),
    sa.Column('last_activity_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
