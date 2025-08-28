from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base, session


class MarketRequest(Base):
    __tablename__ = "market_requests"
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, nullable=False)  # ID of vendor making the request
    vendor_name = Column(String, nullable=False)  # Name for display purposes
    crop_name = Column(String, nullable=False)  # What crop they want to buy
    quantity_kg = Column(Float, nullable=False)  # How much they want
    max_price_per_kg = Column(Float, nullable=False)  # Maximum they'll pay
    request_date = Column(DateTime, default=datetime.now)
    status = Column(String, default="active")  # active, completed, expired
    contact_info = Column(String)  # Phone number or location for contact
    
    def __repr__(self):
        return f"<MarketRequest(vendor='{self.vendor_name}', crop='{self.crop_name}', quantity={self.quantity_kg}kg, max_price=KSH {self.max_price_per_kg}/kg)>"
    
    @classmethod
    def create(cls, vendor_id, vendor_name, crop_name, quantity_kg, max_price_per_kg, contact_info=""):
        request = cls(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            crop_name=crop_name,
            quantity_kg=quantity_kg,
            max_price_per_kg=max_price_per_kg,
            contact_info=contact_info
        )
        session.add(request)
        session.commit()
        return request
    
    @classmethod
    def get_all(cls):
        return session.query(cls).filter_by(status="active").order_by(cls.request_date.desc()).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_crop(cls, crop_name):
        return session.query(cls).filter_by(crop_name=crop_name, status="active").all()
    
    def mark_completed(self):
        self.status = "completed"
        session.commit()
    
    def delete(self):
        session.delete(self)
        session.commit()
