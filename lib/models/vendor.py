from sqlalchemy import Column, Integer, String
from . import Base, session
from sqlalchemy.orm import relationship


class Vendor(Base):
    __tablename__ = "vendors"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vendor_type = Column(String, nullable=False)  # farmer, middleman, wholesaler
    phone_number = Column(String)
    location = Column(String)  # home location
    
    sales = relationship("Sale", back_populates="vendor", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Vendor(name='{self.name}', type='{self.vendor_type}')>"
    
    @classmethod
    def create(cls, name, vendor_type, phone_number="", location=""):
        vendor = cls(name=name, vendor_type=vendor_type, phone_number=phone_number, location=location)
        session.add(vendor)
        session.commit()
        return vendor
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_type(cls, vendor_type):
        return session.query(cls).filter_by(vendor_type=vendor_type).all()
    
    def delete(self):
        session.delete(self)
        session.commit()