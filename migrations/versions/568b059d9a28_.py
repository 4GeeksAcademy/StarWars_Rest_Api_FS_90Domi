"""empty message

Revision ID: 568b059d9a28
Revises: 3414a5d3b8d5
Create Date: 2025-02-10 23:04:18.212223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '568b059d9a28'
down_revision = '3414a5d3b8d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('terreno', sa.String(length=20), nullable=False))
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('terreno')

    # ### end Alembic commands ###
