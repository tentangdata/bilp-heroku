"""empty message

Revision ID: f5222f90e96a
Revises: f25bf43acb87
Create Date: 2017-03-07 21:14:40.462744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f5222f90e96a'
down_revision = 'f25bf43acb87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('salt', sa.String(length=255), nullable=True))
    op.drop_column('user', 'authenticated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('authenticated', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('user', 'salt')
    # ### end Alembic commands ###