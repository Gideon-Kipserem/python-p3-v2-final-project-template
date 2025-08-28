from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the database engine
engine = create_engine("sqlite:///kenyan_market.db")

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create base class
Base = declarative_base()

# Import models
from .vendor import Vendor
from .crop import Crop
from .sale import Sale
from .market_request import MarketRequest

# Create tables
Base.metadata.create_all(engine)
