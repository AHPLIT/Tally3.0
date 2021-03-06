"""simplified database

Revision ID: 25c5d6ce597d
Revises: 
Create Date: 2020-07-30 11:02:12.169180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c5d6ce597d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('queries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q_type', sa.Text(), nullable=False),
    sa.Column('department', sa.Text(), nullable=False),
    sa.Column('date', sa.Text(), nullable=False),
    sa.Column('time', sa.Text(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=False),
    sa.Column('referral', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('queries')
    # ### end Alembic commands ###
