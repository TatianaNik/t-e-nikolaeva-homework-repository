"""First commit

Revision ID: 9050df7c03d6
Revises: 
Create Date: 2021-10-31 15:24:43.622905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9050df7c03d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homework',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['persons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('homework_done', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['persons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('homeworkresult',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('solution', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homeworkresult')
    op.drop_table('teachers')
    op.drop_table('students')
    op.drop_table('persons')
    op.drop_table('homework')
    # ### end Alembic commands ###
