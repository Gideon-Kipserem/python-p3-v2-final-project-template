from sqlalchemy import Column, Integer, String
from . import Base, session
from sqlalchemy.orm import relationship


class Crop(Base):
    __tablename__ = "crops"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    season = Column(String)  # planting, harvesting, available
    market_section = Column(String)  # vegetables, grains, fruits
    
    sales = relationship("Sale", back_populates="crop", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Crop(name='{self.name}', season='{self.season}')>"
    
    @classmethod
    def create(cls, name, season="", market_section=""):
        crop = cls(name=name, season=season, market_section=market_section)
        session.add(crop)
        session.commit()
        return crop
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_season(cls, season):
        return session.query(cls).filter_by(season=season).all()