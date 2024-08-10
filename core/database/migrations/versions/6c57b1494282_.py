"""

Empty message

Revision ID: 6c57b1494282
Revises: SeaJoba Data
Create Date: 2024-08-10 23:04:49.036977

"""


from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '6c57b1494282'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'charter',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('info', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'country',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('flag', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('flag_union', sa.String(), nullable=True),
        sa.Column('name_union', sa.String(), nullable=True),
        sa.Column('nationality', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('flag'),
        sa.UniqueConstraint('name'),
        sa.UniqueConstraint('nationality')
    )
    op.create_table(
        'crew',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('composition', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('composition')
    )
    op.create_table(
        'fleet',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'location',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('area', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('area')
    )
    op.create_table(
        'position',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('blocked', sa.Boolean(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'city',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
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
        'type',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('fleet_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['fleet_id'], ['fleet.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'company',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('site', sa.String(), nullable=False),
        sa.Column('info', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('city_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['city_id'], ['city.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'vessel',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('type_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['type_id'], ['type.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'manager',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('phone', sa.String(), nullable=False),
        sa.Column('whatsapp', sa.Boolean(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
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
        sa.Column('whatsapp', sa.Boolean(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('birth', sa.DateTime(), nullable=False),
        sa.Column('application', sa.String(), nullable=True),
        sa.Column('openwork', sa.Boolean(), nullable=False),
        sa.Column('nationality_id', sa.BigInteger(), nullable=False),
        sa.Column('vessel_id', sa.BigInteger(), nullable=True),
        sa.Column('rank_id', sa.BigInteger(), nullable=False),
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['nationality_id'], ['country.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['rank_id'], ['rank.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vessel_id'], ['vessel.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'vacancy',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('salary', sa.Integer(), nullable=False),
        sa.Column('duration', sa.String(), nullable=True),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.Column('deadweight', sa.Integer(), nullable=True),
        sa.Column('requirements', sa.String(), nullable=True),
        sa.Column('embarkation', sa.DateTime(), nullable=False),
        sa.Column('location_id', sa.BigInteger(), nullable=True),
        sa.Column('charter_id', sa.BigInteger(), nullable=True),
        sa.Column('crew_id', sa.BigInteger(), nullable=True),
        sa.Column('vessel_id', sa.BigInteger(), nullable=False),
        sa.Column('rank_id', sa.BigInteger(), nullable=False),
        sa.Column('manager_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['charter_id'], ['charter.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['crew_id'], ['crew.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['location_id'], ['location.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['manager_id'], ['manager.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['rank_id'], ['rank.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vessel_id'], ['vessel.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'citizenship',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('vacancy_id', sa.BigInteger(), nullable=False),
        sa.Column('country_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vacancy_id'], ['vacancy.id'], ondelete='CASCADE'),
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
        'preview',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('sailor_id', sa.BigInteger(), nullable=False),
        sa.Column('vacancy_id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['sailor_id'], ['sailor.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['vacancy_id'], ['vacancy.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('preview')
    op.drop_table('favourite')
    op.drop_table('citizenship')
    op.drop_table('vacancy')
    op.drop_table('sailor')
    op.drop_table('manager')
    op.drop_table('vessel')
    op.drop_table('company')
    op.drop_table('type')
    op.drop_table('rank')
    op.drop_table('city')
    op.drop_table('user')
    op.drop_table('position')
    op.drop_table('location')
    op.drop_table('fleet')
    op.drop_table('crew')
    op.drop_table('country')
    op.drop_table('charter')
