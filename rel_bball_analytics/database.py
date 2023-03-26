import logging

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger(__name__)


def save_records(model: db.Model, items: list):
    """Add records to db, log error if one is raised"""
    records = [model(**item) for item in items]

    try:
        db.session.add_all(records)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

        failed_ids = [item["id"] for item in items]
        logger.error(f"Failed to save records with ids: {failed_ids}")


def fetch_records(model: db.Model, or_clause=None, **kwargs):
    """Query model and return matching records"""
    records = query(model=model, or_clause=or_clause, **kwargs).all()
    return [record.__dict__ for record in records]


def delete_records(model: db.Model, or_clause=None, **kwargs):
    """Delete all records in model matching query"""
    query(model=model, or_clause=or_clause, **kwargs).delete(synchronize_session=False)
    db.session.commit()


def query(model: db.Model, or_clause: dict, **kwargs):
    """Execute query given model and filter arguments"""
    query = db.session.query(model).filter_by(**kwargs)

    if or_clause is None:
        return query

    return query.filter(
        or_(getattr(model, key) == val for key, val in or_clause.items())
    )
