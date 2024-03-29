"""empty message

Revision ID: d5147f6e9cfa
Revises: 9a837c202781
Create Date: 2023-06-10 14:47:39.870734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5147f6e9cfa'
down_revision = '9a837c202781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint('email', 'users', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('email', 'users', type_='unique')
    op.drop_column('users', 'email')


    # ### end Alembic commands ###
