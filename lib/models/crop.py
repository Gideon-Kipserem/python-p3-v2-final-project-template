from sqlalchemy import Column, Integer, String
from . import Base, session
from sqlalchemy.orm import relationship

# Crop table
class Crop(Base):
    __tablename__ = "crops"
    
    # Columns
    id = Column(Integer, primary_key=True)   # primary key
    name = Column(String, nullable=False)    # crop name
    season = Column(String)                  # planting, harvesting, available
    market_section = Column(String)          # vegetables, grains, fruits
    
    # One crop -> many sales
    sales = relationship("Sale", back_populates="crop", cascade="all, delete-orphan")
    
    # Print format
    def __repr__(self):
        return f"<Crop(name='{self.name}', season='{self.season}')>"
    
    # Create new crop
    @classmethod
    def create(cls, name, season="", market_section=""):
        crop = cls(name=name, season=season, market_section=market_section)
        session.add(crop)
        session.commit()
        return crop
    
    # Get all crops
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    # Find crop by id
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    # Find crops by season
    @classmethod
    def find_by_season(cls, season):
        return session.query(cls).filter_by(season=season).all()
