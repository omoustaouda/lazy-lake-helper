from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Config

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Chore(Base):
    __tablename__ = 'chores'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    task = Column(String, nullable=False)

Base.metadata.create_all(engine)
