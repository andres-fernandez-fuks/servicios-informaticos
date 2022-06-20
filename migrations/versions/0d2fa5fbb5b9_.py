"""adds change_id to all item versions and drafts

Revision ID: 0d2fa5fbb5b9
Revises: a7911f952b52
Create Date: 2022-06-20 16:28:03.606928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d2fa5fbb5b9'
down_revision = 'd50e91125419'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item_hardware_version', sa.Column('change_id', sa.Integer(), nullable=True))
    op.create_foreign_key('hardware_version_change_id', 'item_hardware_version', 'change', ['change_id'], ['id'])
    op.add_column('item_sla_version', sa.Column('change_id', sa.Integer(), nullable=True))
    op.create_foreign_key('sla_version_change_id', 'item_sla_version', 'change', ['change_id'], ['id'])
    op.add_column('item_software_version', sa.Column('change_id', sa.Integer(), nullable=True))
    op.create_foreign_key('software_version_change_id', 'item_software_version', 'change', ['change_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('software_version_change_id', 'item_software_version', type_='foreignkey')
    op.drop_column('item_software_version', 'change_id')
    op.drop_constraint('sla_version_change_id', 'item_sla_version', type_='foreignkey')
    op.drop_column('item_sla_version', 'change_id')
    op.drop_constraint('hardware_version_change_id', 'item_hardware_version', type_='foreignkey')
    op.drop_column('item_hardware_version', 'change_id')
    # ### end Alembic commands ###
