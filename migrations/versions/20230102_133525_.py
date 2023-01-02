"""empty message

Revision ID: 61a427b8d29c
Revises: e08cf2051b6d
Create Date: 2023-01-02 13:35:25.141000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61a427b8d29c'
down_revision = 'e08cf2051b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('team1id', sa.Integer()),
    sa.Column('team2id', sa.Integer()),
    sa.ForeignKeyConstraint(['team1id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['team2id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
