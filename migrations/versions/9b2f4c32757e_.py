""" Added last version to known error

Revision ID: 9b2f4c32757e
Revises: 0d2fa5fbb5b9
Create Date: 2022-06-23 20:13:27.856569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b2f4c32757e'
down_revision = '0d2fa5fbb5b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('known_error', sa.Column('last_version', sa.SmallInteger(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('known_error', 'last_version')
    # ### end Alembic commands ###