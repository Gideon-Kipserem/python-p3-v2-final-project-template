from sqlalchemy import Column, Integer, String
from . import Base, session
from sqlalchemy.orm import relationship

# Vendor table
class Vendor(Base):
    __tablename__ = "vendors"
    
    # Columns
    id = Column(Integer, primary_key=True)         # primary key
    name = Column(String, nullable=False)          # vendor name
    vendor_type = Column(String, nullable=False)   # farmer, middleman, wholesaler
    phone_number = Column(String)                  # contact
    location = Column(String)                      # home location
    
    # One vendor -> many sales
    sales = relationship("Sale", back_populates="vendor", cascade="all, delete-orphan")
    
    # Print format
    def __repr__(self):
        return f"<Vendor(name='{self.name}', type='{self.vendor_type}')>"
    
    # Create vendor
    @classmethod
    def create(cls, name, vendor_type, phone_number="", location=""):
        vendor = cls(name=name, vendor_type=vendor_type, phone_number=phone_number, location=location)
        session.add(vendor)
        session.commit()
        return vendor
    
    # Get all vendors
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    # Find vendor by id
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    # Find vendors by type
    @classmethod
    def find_by_type(cls, vendor_type):
        return session.query(cls).filter_by(vendor_type=vendor_type).all()
    
    # Delete vendor
    def delete(self):
        session.delete(self)
        session.commit()
