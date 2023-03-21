from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from rel_bball_analytics.database import db


class Game(db.Model):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    season = Column(Integer(), nullable=False)
    date = Column(DateTime(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    home = Column(String(8))
    away = Column(String(8))
    home_score = Column(Integer())
    away_score = Column(Integer())
    winner = Column(String(8))
    difference = Column(Integer())
