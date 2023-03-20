from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from rel_bball_analytics.database import db


class Statistic(db.Model):
    __tablename__ = "statistics"

    id = Column(String(16), primary_key=True)
    player_id = Column(Integer(), nullable=False)
    game_id = Column(Integer(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    season = Column(Integer(), nullable=False)
    team_id = Column(Integer(), nullable=False)
    team = Column(String(8))
    position = Column(String(8))

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
