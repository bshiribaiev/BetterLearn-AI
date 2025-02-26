"""Add subjects and subject_id to topics

Revision ID: 66fccafb5020
Revises: 3aac6ab2aa21
Create Date: 2024-11-07 09:17:27.307810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66fccafb5020'
down_revision = '3aac6ab2aa21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subject')
    # ### end Alembic commands ###
