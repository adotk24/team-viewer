"""empty message

Revision ID: 68cfb6907284
Revises: 61a427b8d29c
Create Date: 2023-01-08 17:20:15.464743

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '68cfb6907284'
down_revision = '61a427b8d29c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teamid', sa.Integer(), nullable=True),
    sa.Column('gameid', sa.Integer, nullable=True),
    sa.Column('playerid', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('rebounds', sa.Integer(), nullable=True),
    sa.Column('assists', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playerid'], ['players.id'], ),
    sa.ForeignKeyConstraint(['teamid'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['gameid'], ['games.id']),
    sa.PrimaryKeyConstraint('id')
    )
    # op.alter_column('teams', 'userId',
    #            existing_type=sa.INTEGER(),
    #            nullable=True)
    # op.create_foreign_key(None, 'teams', 'users', ['userId'], ['id'])
    # op.drop_column('teams', 'year')
    if environment == "production":
        op.execute(f"ALTER TABLE stats SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    # ### end Alembic commands ###
