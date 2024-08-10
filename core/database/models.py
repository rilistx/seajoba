from sqlalchemy import func, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    __abstract__ = True

    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    flag: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(unique=True)
    flag_union: Mapped[str | None]
    name_union: Mapped[str | None]
    nationality: Mapped[str] = mapped_column(unique=True)


class City(Base):
    __tablename__ = 'city'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    country_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('country.id', ondelete='CASCADE'))

    country: Mapped['Country'] = relationship(backref='city')


class Location(Base):
    __tablename__ = 'location'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(unique=True)


class Crew(Base):
    __tablename__ = 'crew'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    composition: Mapped[str] = mapped_column(unique=True)


class Charter(Base):
    __tablename__ = 'charter'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    info: Mapped[str]


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str]
    email: Mapped[str]
    site: Mapped[str]
    info: Mapped[str]
    address: Mapped[str]
    city_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('city.id', ondelete='CASCADE'))

    city: Mapped['City'] = relationship(backref='company')


class Fleet(Base):
    __tablename__ = 'fleet'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)


class Type(Base):
    __tablename__ = 'type'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    fleet_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('fleet.id', ondelete='CASCADE'))

    fleet: Mapped['Fleet'] = relationship(backref='type')


class Vessel(Base):
    __tablename__ = 'vessel'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    type_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('type.id', ondelete='CASCADE'))

    type: Mapped['Type'] = relationship(backref='vessel')


class Position(Base):
    __tablename__ = 'position'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)


class Rank(Base):
    __tablename__ = 'rank'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    position_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('position.id', ondelete='CASCADE'))

    position: Mapped['Position'] = relationship(backref='rank')


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[str]
    first_name: Mapped[str | None]
    blocked: Mapped[bool] = mapped_column(default=False)


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    phone: Mapped[str]
    whatsapp: Mapped[bool]
    email: Mapped[str]
    company_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('company.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    company: Mapped['Company'] = relationship(backref='manager')
    user: Mapped['User'] = relationship(backref='manager')


class Sailor(Base):
    __tablename__ = 'sailor'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    phone: Mapped[str]
    whatsapp: Mapped[bool]
    email: Mapped[str]
    birth: Mapped[DateTime] = mapped_column(DateTime)
    application: Mapped[str | None]
    openwork: Mapped[bool]
    nationality_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('country.id', ondelete='CASCADE'))
    vessel_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('vessel.id', ondelete='CASCADE'))
    rank_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('rank.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    nationality: Mapped['Country'] = relationship(backref='sailor')
    vessel: Mapped['Vessel'] = relationship(backref='sailor')
    rank: Mapped['Rank'] = relationship(backref='sailor')
    user: Mapped['User'] = relationship(backref='sailor')


class Vacancy(Base):
    __tablename__ = 'vacancy'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    salary: Mapped[int]
    duration: Mapped[str | None]
    age: Mapped[int | None]
    deadweight: Mapped[int | None]
    requirements: Mapped[str | None]
    embarkation: Mapped[DateTime] = mapped_column(DateTime)
    location_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('location.id', ondelete='CASCADE'))
    charter_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('charter.id', ondelete='CASCADE'))
    crew_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('crew.id', ondelete='CASCADE'))
    vessel_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vessel.id', ondelete='CASCADE'))
    rank_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('rank.id', ondelete='CASCADE'))
    manager_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('manager.id', ondelete='CASCADE'))\

    location: Mapped['Location'] = relationship(backref='vacancy')
    charter: Mapped['Charter'] = relationship(backref='vacancy')
    crew: Mapped['Crew'] = relationship(backref='vacancy')
    vessel: Mapped['Vessel'] = relationship(backref='vacancy')
    rank: Mapped['Rank'] = relationship(backref='vacancy')
    manager: Mapped['Manager'] = relationship(backref='vacancy')


class Citizenship(Base):
    __tablename__ = 'citizenship'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))
    country_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('country.id', ondelete='CASCADE'))

    vacancy: Mapped['Vacancy'] = relationship(backref='citizenship')
    country: Mapped['Country'] = relationship(backref='citizenship')


class Preview(Base):
    __tablename__ = 'preview'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    sailor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sailor.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    sailor: Mapped['Sailor'] = relationship(backref='preview')
    vacancy: Mapped['Vacancy'] = relationship(backref='preview')


class Favourite(Base):
    __tablename__ = 'favourite'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    sailor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sailor.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    sailor: Mapped['Sailor'] = relationship(backref='favourite')
    vacancy: Mapped['Vacancy'] = relationship(backref='favourite')
