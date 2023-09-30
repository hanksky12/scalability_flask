import logging
import typing
from dataclasses import dataclass
from typing import List

from sqlalchemy import create_engine, select, update, insert, delete, func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute


@dataclass(frozen=True)
class SqlCond:
    column: InstrumentedAttribute = None
    value: str = None
    op: str = "="  # in,  <

    def __post_init__(self):
        if self.column is None or self.value is None:
            raise ValueError("column 和 value 必須同時存在或同時不存在")


@dataclass(frozen=True)
class SqlJoin:
    table: typing.Any = None
    relation: InstrumentedAttribute = None

    def __post_init__(self):
        if self.table is None or self.relation is None:
            raise ValueError("table 和 relation 必須同時存在或同時不存在")


@dataclass(frozen=True)
class SqlOrder:
    column: InstrumentedAttribute = None


class SqlUtil:
    engine = None
    Session = None
    table = None

    @classmethod
    def init(cls, user: str, password: str, host: str, port: str, db: str):
        cls.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8",
            pool_size=30,
            max_overflow=0,
            pool_recycle=3600)

        session_factory = sessionmaker(bind=cls.engine)
        '''
        a Session local to the thread ＝> thread safe
        see https://docs.sqlalchemy.org/en/20/orm/contextual.html#unitofwork-contextual
        '''
        cls.Session = scoped_session(session_factory)
        logging.info("SqlUtil init success")

    @classmethod
    def select(cls,
               table,
               cond_list: List[SqlCond] = [],
               join_list: List[SqlJoin] = [],
               order_by: SqlOrder = SqlOrder(),
               first_row: bool = False
               ):
        cls.table = table
        stmt = cls.__create_stmt("select", cond_list, join_list, order_by, {})
        with cls.Session() as session:
            result = session.execute(stmt)
            if result is None:
                return None
            if first_row:
                return result.scalar()
            if len(join_list) > 0:
                return result.all()
            return [row[0] for row in result]
    #...