"""Project dependency"""
from app.database import SessionLocal


def get_db():
    """Open db session and close after method run"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
