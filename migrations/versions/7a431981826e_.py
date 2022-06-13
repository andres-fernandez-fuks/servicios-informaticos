"""added incident and problem relationship to change

Revision ID: 7a431981826e
Revises: adef00e99cb4
Create Date: 2022-06-08 20:57:00.617204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a431981826e'
down_revision = 'adef00e99cb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('incident_change',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.Column('change_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['change_id'], ['change.id'], ),
    sa.ForeignKeyConstraint(['incident_id'], ['incident.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('problem_change',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('change_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['change_id'], ['change.id'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['problem.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('problem_change')
    op.drop_table('incident_change')
    # ### end Alembic commands ###