from typing import Type, TypeVar, Generic, Union, Sequence, Any

from sqlalchemy import select, Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.database.engine import async_session


Table = TypeVar('Table', bound='BaseModel')


class BaseQuerySet(Generic[Table]):
    def __init__(self, session: AsyncSession, model: Type[Table]):
        self.session = session
        self.model = model
        self.query = select(self.model)

    async def create(self, **kwargs) -> Table:
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def update(self, instance: Table, **kwargs) -> Table:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def delete(self, instance: Table) -> None:
        await self.session.delete(instance)
        await self.session.commit()

    async def get(self, **kwargs) -> Table:
        self.query = self.query.filter_by(**kwargs)
        result = await self.session.execute(self.query)
        return result.scalars().one()

    def select(self, *args) -> 'BaseQuerySet':
        self.query = select(*args)
        return self

    def filter(self, *args, **kwargs) -> 'BaseQuerySet':
        self.query = self.query.filter(*args).filter_by(**kwargs)
        return self

    def order_by(self, *args) -> 'BaseQuerySet':
        self.query = self.query.order_by(*args)
        return self

    def join(self, target, *args, isouter=False, full=False, **kwargs) -> 'BaseQuerySet':
        self.query = self.query.join(target, *args, isouter=isouter, full=full, **kwargs)
        return self

    def group_by(self, *args) -> 'BaseQuerySet':
        self.query = self.query.group_by(*args)
        return self

    def having(self, *args) -> 'BaseQuerySet':
        self.query = self.query.having(*args)
        return self

    async def first(self, limit: int = 1) -> Union[None, Table, Sequence[Table]]:
        self.query = self.query.limit(limit)
        result = await self.session.execute(self.query)
        return result.scalars().all() if limit > 1 else result.scalars().first()

    async def one(self) -> Union[None, Table]:
        result = await self.session.execute(self.query)
        return result.scalars().one_or_none()

    async def all(self) -> Union[None, Sequence[Table]]:
        result = await self.session.execute(self.query)
        return result.scalars().all()

    async def onr(self) -> Union[None, Table]:
        result = await self.session.execute(self.query)
        return result.one_or_none()

    async def alr(self) -> Union[None, Sequence[Row[tuple[Any]]]]:
        result = await self.session.execute(self.query)
        return result.all()


class BaseModel(DeclarativeBase):
    __abstract__ = True

    @classmethod
    async def create(cls, **kwargs) -> Table:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.create(**kwargs)

    @classmethod
    async def update(cls, instance: Table, **kwargs) -> Table:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.update(instance, **kwargs)

    @classmethod
    async def delete(cls, instance: Table) -> None:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.delete(instance)

    @classmethod
    async def get(cls, **kwargs) -> Table:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.get(**kwargs)

    @classmethod
    def filter(cls, *args, **kwargs) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.filter(*args, **kwargs)

    @classmethod
    def select(cls, *args) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.select(*args)

    @classmethod
    def order_by(cls, *args) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.order_by(*args)

    @classmethod
    def join(cls, target, *args, onclause=None, isouter=False, full=False, **kwargs) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.join(target, *args, onclause, isouter, full, **kwargs)

    @classmethod
    def group_by(cls, *args) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.group_by(*args)

    @classmethod
    def having(cls, *args) -> 'BaseQuerySet':
        session = async_session()
        queryset = BaseQuerySet(session, cls)
        return queryset.having(*args)

    @classmethod
    async def first(cls, limit: int = 1) -> 'BaseQuerySet':
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.first(limit)

    @classmethod
    async def one(cls) -> Union[None, Table]:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.one()

    @classmethod
    async def all(cls) -> Union[None, Sequence[Table]]:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.all()

    @classmethod
    async def onr(cls) -> Union[None, Table]:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.onr()

    @classmethod
    async def alr(cls) -> Union[None, Sequence[Row[tuple[Any]]]]:
        async with async_session() as session:
            queryset = BaseQuerySet(session, cls)
            return await queryset.alr()
