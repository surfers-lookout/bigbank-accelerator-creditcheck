from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import IntegrityError
from main.logger import logger
from . import Base
from . import SessionLocal

# Dummy table for an example
class Dummy(Base):
    __tablename__ = 'dummy'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, index=True)
    comment = Column(String(64), unique=False, index=True)

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        self.id = self.add()

    def __repr__(self):
        return self.id

    def add(self):
        _id = None
        _session = SessionLocal()
        _session.add(self)
        try:
            _session.commit()
            logger.info('Dummy Record Added: %s', self.name)
        except IntegrityError:
            _session.rollback()

        if self.id is None:
            _resp = Dummy.query.with_entities(Dummy.id).filter(Dummy.name == self.name).first()
            _id = _resp.id
        else:
            _id = self.id

        return _id

    @staticmethod
    def get():
        _session = SessionLocal()
        result = _session.query(Dummy).all()
        return result





