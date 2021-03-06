"""trytofixshortener

Revision ID: 6f3f5c6d11a8
Revises: b4a59a7f89ff
Create Date: 2021-12-09 23:35:19.169554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f3f5c6d11a8'
down_revision = 'b4a59a7f89ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shortened_link', 'link',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('shortened_link', 'linkHash',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shortened_link', 'linkHash',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('shortened_link', 'link',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###
