"""

Empty message

Revision ID: 212aec6cbbd2
Revises: SeaJoba Data
Create Date: 2024-07-07 17:37:51.288522

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '212aec6cbbd2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'charter',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('info', sa.String(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'country',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('flag', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'fleet',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'location',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'nationality',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'position',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'premium',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('manager', sa.Integer(), nullable=False),
        sa.Column('seamen', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False),
        sa.Column('premium', sa.Boolean(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'company',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('site', sa.String(), nullable=True),
        sa.Column('info', sa.String(), nullable=True),
        sa.Column('start', sa.DateTime(), nullable=False),
        sa.Column('country_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'rank',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('position_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['position_id'], ['position.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'vessel',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('fleet_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['fleet_id'], ['fleet.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'manager',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('whatsapp', sa.Boolean(), nullable=False),
        sa.Column('company_id', sa.BigInteger(), nullable=False),
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'sailor',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('whatsapp', sa.Boolean(), nullable=False),
        sa.Column('openwork', sa.Boolean(), nullable=False),
        sa.Column('application', sa.String(), nullable=False),
        sa.Column('birth', sa.DateTime(), nullable=False),
        sa.Column('nationality_id', sa.BigInteger(), nullable=False),
        sa.Column('rank_id', sa.BigInteger(), nullable=False),
        sa.Column('vessel_id', sa.BigInteger(), nullable=False),
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['nationality_id'], ['nationality.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['rank_id'], ['rank.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vessel_id'], ['vessel.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'vacancy',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('salary', sa.String(), nullable=False),
        sa.Column('duration', sa.String(), nullable=False),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.Column('deadweight', sa.String(), nullable=True),
        sa.Column('requirements', sa.String(), nullable=True),
        sa.Column('embarkation', sa.DateTime(), nullable=False),
        sa.Column('location_id', sa.BigInteger(), nullable=True),
        sa.Column('charter_id', sa.BigInteger(), nullable=True),
        sa.Column('nationality_id', sa.BigInteger(), nullable=True),
        sa.Column('company_id', sa.BigInteger(), nullable=False),
        sa.Column('rank_id', sa.BigInteger(), nullable=False),
        sa.Column('vessel_id', sa.BigInteger(), nullable=False),
        sa.Column('manager_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['charter_id'], ['charter.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['location_id'], ['location.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['manager_id'], ['manager.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['nationality_id'], ['nationality.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['rank_id'], ['rank.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vessel_id'], ['vessel.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'favourite',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('sailor_id', sa.BigInteger(), nullable=False),
        sa.Column('vacancy_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['sailor_id'], ['sailor.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vacancy_id'], ['vacancy.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'view',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('sailor_id', sa.BigInteger(), nullable=False),
        sa.Column('vacancy_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['sailor_id'], ['sailor.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vacancy_id'], ['vacancy.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('view')
    op.drop_table('favourite')
    op.drop_table('vacancy')
    op.drop_table('sailor')
    op.drop_table('manager')
    op.drop_table('vessel')
    op.drop_table('rank')
    op.drop_table('company')
    op.drop_table('user')
    op.drop_table('premium')
    op.drop_table('position')
    op.drop_table('nationality')
    op.drop_table('location')
    op.drop_table('fleet')
    op.drop_table('country')
    op.drop_table('charter')
    # ### end Alembic commands ###
