from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base, session

# Sale table
class Sale(Base):
    __tablename__ = "sales"
    
    # Columns
    id = Column(Integer, primary_key=True)                 # primary key
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)  # vendor link
    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=False)      # crop link
    price_per_kg = Column(Float)                           # price per kg
    quantity_kg = Column(Float)                            # quantity in kg
    market_day = Column(String)                            # e.g. Monday
    transaction_date = Column(DateTime, default=datetime.now)  # date and time
    
    # Relationships
    vendor = relationship("Vendor", back_populates="sales")
    crop = relationship("Crop", back_populates="sales")
    
    # Print format
    def __repr__(self):
        vendor_name = self.vendor.name if self.vendor else "Unknown"
        crop_name = self.crop.name if self.crop else "Unknown"
        total = self.price_per_kg * self.quantity_kg if self.price_per_kg and self.quantity_kg else 0
        date_str = self.transaction_date.strftime("%Y-%m-%d %H:%M") if self.transaction_date else "Unknown"
        return f"<Sale(vendor='{vendor_name}', crop='{crop_name}', total=KSH {total:.2f}, date={date_str})>"
    
    # Create new sale
    @classmethod
    def create(cls, vendor, crop, price_per_kg, quantity_kg, market_day=""):
        sale = cls(vendor=vendor, crop=crop, price_per_kg=price_per_kg, 
                  quantity_kg=quantity_kg, market_day=market_day)
        session.add(sale)
        session.commit()
        return sale
    
    # Get all sales (latest first)
    @classmethod
    def get_all(cls):
        return session.query(cls).order_by(cls.transaction_date.desc()).all()
    
    # Find sale by id
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    # Delete a sale
    def delete(self):
        session.delete(self)
        session.commit()
