#!/usr/bin/env python3
# lib/debug.py

from models import Vendor, Crop, Sale, MarketRequest


def create_sample_data():
    print("Creating Kenyan market sample data...")
    
    # Create sample vendors
    vendor1 = Vendor.create("Mama Sarah", "farmer", "0712345678", "Kisumu")
    vendor2 = Vendor.create("Juma Otieno", "middleman", "0723456789", "Nakuru")
    vendor3 = Vendor.create("Fatima Hassan", "wholesaler", "0734567890", "Mombasa")
    vendor4 = Vendor.create("Peter Kamau", "farmer", "0745678901", "Thika")
    vendor5 = Vendor.create("Grace Wanjiku", "middleman", "0756789012", "Eldoret")
    
    # Create sample crops
    crop1 = Crop.create("Sukuma Wiki", "available", "vegetables")
    crop2 = Crop.create("Maize", "harvesting", "grains")
    crop3 = Crop.create("Irish Potatoes", "available", "tubers")
    crop4 = Crop.create("Tomatoes", "growing", "vegetables")
    crop5 = Crop.create("Sweet Potatoes", "available", "tubers")
    crop6 = Crop.create("Beans", "harvesting", "grains")
    crop7 = Crop.create("Onions", "available", "vegetables")
    crop8 = Crop.create("Bananas", "available", "fruits")
    
    # Create sample sales
    Sale.create(vendor1, crop1, 50.0, 25.0, "Monday")      # Mama Sarah sells Sukuma Wiki
    Sale.create(vendor2, crop2, 80.0, 100.0, "Tuesday")     # Juma sells Maize
    Sale.create(vendor3, crop3, 120.0, 50.0, "Wednesday")   # Fatima sells Irish Potatoes
    Sale.create(vendor4, crop4, 200.0, 15.0, "Thursday")    # Peter sells Tomatoes
    Sale.create(vendor5, crop5, 60.0, 30.0, "Friday")       # Grace sells Sweet Potatoes
    Sale.create(vendor1, crop7, 40.0, 20.0, "Saturday")     # Mama Sarah also sells Onions
    Sale.create(vendor2, crop6, 150.0, 40.0, "Sunday")      # Juma sells Beans
    Sale.create(vendor3, crop8, 80.0, 45.0, "Monday")       # Fatima sells Bananas
    
    # Create sample market requests (buying opportunities)
    MarketRequest.create(
        vendor_id=vendor2.id,
        vendor_name=vendor2.name,
        crop_name="Sukuma Wiki",
        quantity_kg=100.0,
        max_price_per_kg=45.0,
        contact_info="0723456789, Nakuru Market"
    )
    
    MarketRequest.create(
        vendor_id=vendor3.id,
        vendor_name=vendor3.name,
        crop_name="Irish Potatoes",
        quantity_kg=200.0,
        max_price_per_kg=110.0,
        contact_info="0734567890, Mombasa Wholesale"
    )
    
    MarketRequest.create(
        vendor_id=vendor5.id,
        vendor_name=vendor5.name,
        crop_name="Tomatoes",
        quantity_kg=50.0,
        max_price_per_kg=180.0,
        contact_info="0756789012, Eldoret"
    )
    
    print("✅ Sample Kenyan market data created successfully!")
    print(f"   - {5} vendors (farmers, middlemen, wholesalers)")
    print(f"   - {8} crops (vegetables, grains, fruits, tubers)")
    print(f"   - {8} sales transactions")
    print(f"   - {3} market requests (buying opportunities)")


if __name__ == "__main__":
    create_sample_data()
