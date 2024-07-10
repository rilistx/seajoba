from sqlalchemy import func, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    __abstract__ = True

    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Premium(Base):
    __tablename__ = 'premium'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    sailor: Mapped[int]
    manager: Mapped[int]

    def __str__(self):
        return f'Premium ID: {self.id}'


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    flag: Mapped[str]

    def __str__(self):
        return f'Country ID: {self.id}'


class City(Base):
    __tablename__ = 'city'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    country_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('country.id', ondelete='CASCADE'))

    country: Mapped['Country'] = relationship(backref='city')

    def __str__(self):
        return f'City ID: {self.id}'


class Nationality(Base):
    __tablename__ = 'nationality'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Nationality ID: {self.id}'


class Location(Base):
    __tablename__ = 'location'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Location ID: {self.id}'


class Charter(Base):
    __tablename__ = 'charter'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    info: Mapped[str | None]

    def __str__(self):
        return f'Charter ID: {self.id}'


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    site: Mapped[str | None]
    info: Mapped[str | None]
    start: Mapped[DateTime] = mapped_column(DateTime)
    city_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('city.id', ondelete='CASCADE'))

    city: Mapped['City'] = relationship(backref='company')

    def __str__(self):
        return f'Company ID: {self.id}'


class Position(Base):
    __tablename__ = 'position'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Position ID: {self.id}'


class Rank(Base):
    __tablename__ = 'rank'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    position_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('position.id', ondelete='CASCADE'))

    position: Mapped['Position'] = relationship(backref='rank')

    def __str__(self):
        return f'Rank ID: {self.id}'


class Fleet(Base):
    __tablename__ = 'fleet'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Fleet ID: {self.id}'


class Vessel(Base):
    __tablename__ = 'vessel'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    fleet_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('fleet.id', ondelete='CASCADE'))

    fleet: Mapped['Fleet'] = relationship(backref='vessel')

    def __str__(self):
        return f'Vessel ID: {self.id}'


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[str]
    premium: Mapped[bool]
    first_name: Mapped[str | None]
    active: Mapped[bool] = mapped_column(default=True)
    blocked: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f'User ID: {self.id}'


class Sailor(Base):
    __tablename__ = 'sailor'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    phone: Mapped[str]
    email: Mapped[str]
    whatsapp: Mapped[bool]
    openwork: Mapped[bool]
    application: Mapped[str]
    birth: Mapped[DateTime] = mapped_column(DateTime)
    nationality_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('nationality.id', ondelete='CASCADE'))
    rank_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('rank.id', ondelete='CASCADE'))
    vessel_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('vessel.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    nationality: Mapped['Nationality'] = relationship(backref='sailor')
    rank: Mapped['Rank'] = relationship(backref='sailor')
    vessel: Mapped['Vessel'] = relationship(backref='sailor')
    user: Mapped['User'] = relationship(backref='sailor')

    def __str__(self):
        return f'Sailor ID: {self.id}'


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    phone: Mapped[str]
    email: Mapped[str]
    whatsapp: Mapped[bool]
    company_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('company.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    company: Mapped['Company'] = relationship(backref='manager')
    user: Mapped['User'] = relationship(backref='manager')

    def __str__(self):
        return f'Manager ID: {self.id}'


class Vacancy(Base):
    __tablename__ = 'vacancy'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    salary: Mapped[str]
    duration: Mapped[str]
    age: Mapped[int | None]
    deadweight: Mapped[str | None]
    requirements: Mapped[str | None]
    embarkation: Mapped[DateTime] = mapped_column(DateTime)
    location_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('location.id', ondelete='CASCADE'))
    charter_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('charter.id', ondelete='CASCADE'))
    nationality_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('nationality.id', ondelete='CASCADE'))
    company_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('company.id', ondelete='CASCADE'))
    rank_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('rank.id', ondelete='CASCADE'))
    vessel_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vessel.id', ondelete='CASCADE'))
    manager_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('manager.id', ondelete='CASCADE'))

    location: Mapped['Location'] = relationship(backref='vacancy')
    charter: Mapped['Charter'] = relationship(backref='vacancy')
    nationality: Mapped['Nationality'] = relationship(backref='vacancy')
    company: Mapped['Company'] = relationship(backref='vacancy')
    rank: Mapped['Rank'] = relationship(backref='vacancy')
    vessel: Mapped['Vessel'] = relationship(backref='vacancy')
    manager: Mapped['Manager'] = relationship(backref='vacancy')

    def __str__(self):
        return f'Vacancy ID: {self.id}'


class View(Base):
    __tablename__ = 'view'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    sailor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sailor.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    sailor: Mapped['Sailor'] = relationship(backref='view')
    vacancy: Mapped['Vacancy'] = relationship(backref='view')

    def __str__(self):
        return f'View ID: {self.id}'


class Favourite(Base):
    __tablename__ = 'favourite'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    sailor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sailor.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    sailor: Mapped['Sailor'] = relationship(backref='favourite')
    vacancy: Mapped['Vacancy'] = relationship(backref='favourite')

    def __str__(self):
        return f'Favourite ID: {self.id}'
