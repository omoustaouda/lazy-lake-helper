from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Config

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True)
    item = Column(String, nullable=False)
    location = Column(String, nullable=False)

Base.metadata.create_all(engine)
