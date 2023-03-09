import logging
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from rel_bball_analytics.database import db

logger = logging.getLogger(__name__)


class Player(db.Model):
    __tablename__ = "players"

    id = Column(String(16), primary_key=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    season = Column(Integer(), nullable=False)
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
    team_id = Column(Integer())
    team = Column(String(16))
    position = Column(String(16))

    games_played = Column(Integer())
    points = Column(Float())
    minutes_played = Column(Float())
    field_goals_made = Column(Float())
    field_goal_attempts = Column(Float())
    field_goal_percentage = Column(Float())
    three_points_made = Column(Float())
    three_point_attempts = Column(Float())
    three_point_percentage = Column(Float())
    free_throws_made = Column(Float())
    free_throw_attempts = Column(Float())
    free_throw_percentage = Column(Float())
    offensive_rebounds = Column(Float())
    defensive_rebounds = Column(Float())
    total_rebounds = Column(Float())
    assists = Column(Float())
    steals = Column(Float())
    blocks = Column(Float())
    turnovers = Column(Float())
    personal_fouls = Column(Float())


def save_player_records(players: list):
    """Add player records to db, log error if one is raised"""
    records = [Player(**player) for player in players]

    try:
        db.session.add_all(records)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

        failed_ids = [player["id"] for player in players]
        logger.error(f"Failed to save records with ids: {failed_ids}")


def fetch_player_records(**kwargs):
    """Query players table and return matching records"""
    records = db.session.query(Player).filter_by(**kwargs).all()
    return [record.__dict__ for record in records]
