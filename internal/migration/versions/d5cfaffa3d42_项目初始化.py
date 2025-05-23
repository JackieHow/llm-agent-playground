"""项目初始化

Revision ID: d5cfaffa3d42
Revises: 
Create Date: 2025-04-07 20:51:29.429675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5cfaffa3d42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app',
    sa.Column('id', sa.UUID(), nullable=False, comment='主键'),
    sa.Column('account_id', sa.UUID(), nullable=False, comment='账号ID'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='名称'),
    sa.Column('icon', sa.String(length=255), nullable=True, comment='图标'),
    sa.Column('description', sa.Text(), nullable=True, comment='描述'),
    sa.Column('update_at', sa.DateTime(), nullable=False, comment='更新时间'),
    sa.Column('create_at', sa.DateTime(), nullable=False, comment='创建时间'),
    sa.PrimaryKeyConstraint('id', name='pk_app_id')
    )
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.create_index('idx_app_account_id', ['account_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.drop_index('idx_app_account_id')

    op.drop_table('app')
    # ### end Alembic commands ###
