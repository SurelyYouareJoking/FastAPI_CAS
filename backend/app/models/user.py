from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.orm import Session
from app.models.base import Base


class DBUser(Base):
    __tablename__ = 'test_user'

    id = Column(INTEGER(64), primary_key=True, comment='编号')
    username = Column(String(100))
    last_login = Column(DateTime, nullable=False)
    first_login = Column(DateTime, nullable=False)

    @classmethod
    async def add(cls, db: Session, data):
        db.add(data)
        db.commit()
        # db.refresh(data)

    @classmethod
    async def get_by_username(cls, db: Session, username):
        data = db.query(cls).filter_by(username=username).first()
        return data

    @classmethod
    async def update(cls, db: Session, username, data):
        db.query(cls).filter_by(username=username).update(data)
        db.commit()