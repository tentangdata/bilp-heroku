"""empty message

Revision ID: f25bf43acb87
Revises: 36f9d115ed77
Create Date: 2017-03-07 20:55:47.334466

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f25bf43acb87'
down_revision = '36f9d115ed77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('score_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dictionary_id', sa.Integer(), nullable=True),
    sa.Column('target_user_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dictionary_id'], ['dictionary.id'], ),
    sa.ForeignKeyConstraint(['target_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('word')
    op.add_column(u'dictionary', sa.Column('sentence_id', sa.Integer(), nullable=True))
    op.add_column(u'dictionary', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'dictionary', 'sentence', ['sentence_id'], ['id'])
    op.create_foreign_key(None, 'dictionary', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dictionary', type_='foreignkey')
    op.drop_constraint(None, 'dictionary', type_='foreignkey')
    op.drop_column(u'dictionary', 'user_id')
    op.drop_column(u'dictionary', 'sentence_id')
    op.create_table('word',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('sentence_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('word', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('exist', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['sentence_id'], [u'sentence.id'], name=u'word_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('score_log')
    op.drop_table('user')
    # ### end Alembic commands ###
