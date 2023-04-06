import json
import os
import sys
from unicodedata import category
from . import models, SessionLocal, Base
from main.config import settings
from main.logger import logger



class DataManager():

    @staticmethod
    def initDB():
        logger.info(f'DB URI: {settings.DATABASE_URL}')
        logger.info('Create database')
        
        _localfile = os.path.join(settings.BASEDIR, 'data.sqlite')
        if os.path.exists(_localfile):
            os.remove(_localfile)
        _session = SessionLocal()
        Base.metadata.create_all(_session.bind)
        _session.commit()
        logger.info('Database creation completed')
                
