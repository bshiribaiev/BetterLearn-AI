"""Add next_review and last_reviewed to StudyTopic

Revision ID: 3aac6ab2aa21
Revises: 0aa481bcca99
Create Date: 2024-11-05 07:54:49.239721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aac6ab2aa21'
down_revision = '0aa481bcca99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('study_topic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('study_topic', schema=None) as batch_op:
        batch_op.drop_column('review_count')

    # ### end Alembic commands ###
