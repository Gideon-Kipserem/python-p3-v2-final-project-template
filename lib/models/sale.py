from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base, session


class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=False)
    price_per_kg = Column(Float)
    quantity_kg = Column(Float)
    market_day = Column(String)  # Monday, Tuesday, etc.
    transaction_date = Column(DateTime, default=datetime.now)  # Exact date and time
    
    vendor = relationship("Vendor", back_populates="sales")
    crop = relationship("Crop", back_populates="sales")
    
    def __repr__(self):
        vendor_name = self.vendor.name if self.vendor else "Unknown"
        crop_name = self.crop.name if self.crop else "Unknown"
        total = self.price_per_kg * self.quantity_kg if self.price_per_kg and self.quantity_kg else 0
        date_str = self.transaction_date.strftime("%Y-%m-%d %H:%M") if self.transaction_date else "Unknown"
        return f"<Sale(vendor='{vendor_name}', crop='{crop_name}', total=KSH {total:.2f}, date={date_str})>"
    
    @classmethod
    def create(cls, vendor, crop, price_per_kg, quantity_kg, market_day=""):
        sale = cls(vendor=vendor, crop=crop, price_per_kg=price_per_kg, 
                  quantity_kg=quantity_kg, market_day=market_day)
        session.add(sale)
        session.commit()
        return sale
    
    @classmethod
    def get_all(cls):
        return session.query(cls).order_by(cls.transaction_date.desc()).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    def delete(self):
        session.delete(self)
        session.commit()


