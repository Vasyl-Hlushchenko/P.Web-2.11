from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    birthaday = Column(Date, nullable=False)
    description = Column(String, nullable=True)
