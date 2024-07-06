from sqlalchemy import func, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.queryset import BaseModel


class Base(BaseModel):
    __abstract__ = True

    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Premium(Base):
    __tablename__ = 'premium'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    manager: Mapped[int] = mapped_column(default=0)
    seamen: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return f'Premium ID: {self.id}'


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    flag: Mapped[str]

    def __str__(self):
        return f'Country name: {self.name} ({self.id})'


class Nationality(Base):
    __tablename__ = 'nationality'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Nationality: {self.name} ({self.id})'


class Location(Base):
    __tablename__ = 'location'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Location: {self.name} ({self.id})'


class Charter(Base):
    __tablename__ = 'charter'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    info: Mapped[str | None]

    def __str__(self):
        return f'Charter: {self.name} ({self.id})'


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    site: Mapped[str | None]
    info: Mapped[str | None]
    start: Mapped[DateTime] = mapped_column(DateTime)
    country_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('country.id', ondelete='CASCADE'))

    country: Mapped['Country'] = relationship(backref='company')

    def __str__(self):
        return f'Company name: {self.name} ({self.id})'


class Position(Base):
    __tablename__ = 'position'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Position: {self.name} ({self.id})'


class Rank(Base):
    __tablename__ = 'rank'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    position_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('position.id', ondelete='CASCADE'))

    position: Mapped['Position'] = relationship(backref='rank')

    def __str__(self):
        return f'Rank: {self.name} ({self.position_id} / {self.id})'


class Fleet(Base):
    __tablename__ = 'fleet'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]

    def __str__(self):
        return f'Fleet: {self.name} ({self.id})'


class Vessel(Base):
    __tablename__ = 'vessel'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    fleet_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('fleet.id', ondelete='CASCADE'))

    fleet: Mapped['Fleet'] = relationship(backref='vessel')

    def __str__(self):
        return f'Vessel: {self.name} ({self.fleet_id} / {self.id})'


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[str]
    active: Mapped[bool] = mapped_column(default=True)
    premium: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f'User role : {self.role} ({self.id})'


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    whatsapp: Mapped[bool]
    company_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('company.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    company: Mapped['Company'] = relationship(backref='manager')
    user: Mapped['User'] = relationship(backref='manager')

    def __str__(self):
        return f'Manager: {self.first_name} ({self.user_id} / {self.id})'


class Seaman(Base):
    __tablename__ = 'seaman'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    whatsapp: Mapped[bool]
    openwork: Mapped[bool]
    application: Mapped[str]
    birth: Mapped[DateTime] = mapped_column(DateTime)
    nationality_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('nationality.id', ondelete='CASCADE'))
    rank_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('rank.id', ondelete='CASCADE'))
    vessel_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vessel.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('user.id', ondelete='CASCADE'))

    nationality: Mapped['Nationality'] = relationship(backref='seaman')
    rank: Mapped['Rank'] = relationship(backref='seaman')
    vessel: Mapped['Vessel'] = relationship(backref='seaman')
    user: Mapped['User'] = relationship(backref='seaman')

    def __str__(self):
        return f'Seaman: {self.first_name} ({self.user_id} / {self.id})'


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
    seaman_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('seaman.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    seaman: Mapped['Seaman'] = relationship(backref='view')
    vacancy: Mapped['Vacancy'] = relationship(backref='view')

    def __str__(self):
        return f'View ID: {self.id} ({self.seaman_id} / {self.vacancy_id})'


class Favourite(Base):
    __tablename__ = 'favourite'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    seaman_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('seaman.id', ondelete='CASCADE'))
    vacancy_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('vacancy.id', ondelete='CASCADE'))

    seaman: Mapped['Seaman'] = relationship(backref='favourite')
    vacancy: Mapped['Vacancy'] = relationship(backref='favourite')

    def __str__(self):
        return f'Favourite ID: {self.id} ({self.seaman_id} / {self.vacancy_id})'
