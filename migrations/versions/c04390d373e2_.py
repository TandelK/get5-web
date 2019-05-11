"""Include column for preferred names.

Revision ID: c04390d373e2
Revises: ae2ba46fe1a2
Create Date: 2019-05-11 17:10:32.851439

"""

# revision identifiers, used by Alembic.
revision = 'c04390d373e2'
down_revision = 'ae2ba46fe1a2'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('preferred_names', sa.PickleType(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team', 'preferred_names')
    ### end Alembic commands ###
