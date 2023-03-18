import logging

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


def fetch_records(model: db.Model, **kwargs):
    """Query model and return matching records"""
    records = db.session.query(model).filter_by(**kwargs).all()
    return [record.__dict__ for record in records]


def delete_records(model: db.Model, **kwargs):
    """Delete all records in model matching query"""
    db.session.query(model).filter_by(**kwargs).delete()
    db.session.commit()
