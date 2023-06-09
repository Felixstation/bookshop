"""empty message

Revision ID: d45102f213e8
Revises: 14ad55d068e2
Create Date: 2023-02-14 19:04:58.091888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd45102f213e8'
down_revision = '14ad55d068e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('language', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'lang', ['language'], ['id'])
        batch_op.create_foreign_key(None, 'genre', ['genre'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('language')
        batch_op.drop_column('genre')

    # ### end Alembic commands ###
