from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    release_date = Column(DateTime)
    #director = relationship("Director", back_populates="movies")
    
engine = create_engine('postgresql://postgres:sananebe@localhost/top10movies')

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)