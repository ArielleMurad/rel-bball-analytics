from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from rel_bball_analytics.database import db


class Player(db.Model):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    birth_date = Column(String(16))
    age = Column(Integer())
    country = Column(String(32))
    height_feet = Column(Integer())
    height_inches = Column(Integer())
    weight_pounds = Column(Integer())
    jersey = Column(Integer())
    is_active = Column(Boolean())
    start_year = Column(Integer())
    pro_years = Column(Integer())
    college = Column(String(64))
