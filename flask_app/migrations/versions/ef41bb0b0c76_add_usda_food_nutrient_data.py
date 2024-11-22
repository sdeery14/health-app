"""add usda food nutrient data

Revision ID: ef41bb0b0c76
Revises: ed93022b479f
Create Date: 2024-11-21 23:02:54.615538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef41bb0b0c76'
down_revision = 'ed93022b479f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('food_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('measure_unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('abbreviation', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nutrient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unit_name', sa.String(), nullable=False),
    sa.Column('nutrient_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fdc_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('data_type', sa.String(), nullable=False),
    sa.Column('publication_date', sa.DateTime(), nullable=False),
    sa.Column('food_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['food_category_id'], ['food_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fdc_id')
    )
    op.create_table('food_data_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=False),
    sa.Column('data_source_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['data_source_id'], ['data_source.id'], ),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('food_id', 'data_source_id', name='_food_data_source_uc')
    )
    op.create_table('food_nutrient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=False),
    sa.Column('nutrient_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ),
    sa.ForeignKeyConstraint(['nutrient_id'], ['nutrient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('value', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='data_pkey'),
    sa.UniqueConstraint('name', name='data_name_key')
    )
    op.drop_table('food_nutrient')
    op.drop_table('food_data_source')
    op.drop_table('food')
    op.drop_table('nutrient')
    op.drop_table('measure_unit')
    op.drop_table('food_category')
    op.drop_table('data_source')
    # ### end Alembic commands ###
