"""empty message

Revision ID: 8e1f2941a7ad
Revises: 61a427b8d29c
Create Date: 2023-01-02 22:38:02.397725

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '8e1f2941a7ad'
down_revision = '61a427b8d29c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matchup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team1id', sa.Integer(), nullable=True),
    sa.Column('team2id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team1id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['team2id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    # op.create_foreign_key(None, 'teams', 'users', ['userId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matchup')
    # ### end Alembic commands ###
