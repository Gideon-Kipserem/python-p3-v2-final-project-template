from models import Vendor, Crop, Sale, MarketRequest

# Exit program
def exit_program():
    print("Kwaheri! (Goodbye!)")
    exit()

# Add new vendor
def add_vendor():
    name = input("Enter vendor name: ")
    
    # Vendor type menu
    print("Vendor types:")
    print("1. Farmer (small-scale)")
    print("2. Middleman")
    print("3. Wholesaler")
    vendor_type_choice = input("Select vendor type (1-3): ")
    
    vendor_types = {
        "1": "farmer",
        "2": "middleman", 
        "3": "wholesaler"
    }
    
    vendor_type = vendor_types.get(vendor_type_choice, "farmer")
    phone_number = input("Enter phone number (optional): ")
    location = input("Enter location (optional): ")
    
    # Save vendor
    vendor = Vendor.create(name, vendor_type, phone_number, location)
    print(f"Added vendor: {vendor}")

# Show all vendors
def view_vendors():
    vendors = Vendor.get_all()
    if vendors:
        print("All vendors:")
        print(f"{'ID':<5} {'Name':<20} {'Type':<10} {'Phone':<15} {'Location':<15}")
        print("-" * 70)
        for vendor in vendors:
            print(f"{vendor.id:<5} {vendor.name:<20} {vendor.vendor_type:<10} {vendor.phone_number:<15} {vendor.location:<15}")
    else:
        print("No vendors found.")

# Add new crop
def add_crop():
    name = input("Enter crop name: ")
    
    # Season menu
    print("Seasons:")
    print("1. Planting")
    print("2. Growing") 
    print("3. Harvesting")
    print("4. Available")
    season_choice = input("Select season (1-4): ")
    
    seasons = {
        "1": "planting",
        "2": "growing",
        "3": "harvesting",
        "4": "available"
    }
    
    season = seasons.get(season_choice, "available")
    
    # Market section menu
    print("Market sections:")
    print("1. Vegetables")
    print("2. Grains")
    print("3. Fruits")
    print("4. Tubers")
    section_choice = input("Select market section (1-4): ")
    
    sections = {
        "1": "vegetables",
        "2": "grains",
        "3": "fruits",
        "4": "tubers"
    }
    
    market_section = sections.get(section_choice, "vegetables")
    
    # Save crop
    crop = Crop.create(name, season, market_section)
    print(f"Added crop: {crop}")

# Show all crops
def view_crops():
    crops = Crop.get_all()
    if crops:
        print("All crops:")
        print(f"{'ID':<5} {'Name':<20} {'Season':<12} {'Section':<12}")
        print("-" * 50)
        for crop in crops:
            print(f"{crop.id:<5} {crop.name:<20} {crop.season:<12} {crop.market_section:<12}")
    else:
        print("No crops found.")

# Find vendor by ID
def find_vendor():
    vendor_id = input("Enter vendor ID: ")
    try:
        vendor = Vendor.find_by_id(int(vendor_id))
        if vendor:
            print(f"Found vendor: {vendor}")
            print(f"  Type: {vendor.vendor_type}")
            print(f"  Phone: {vendor.phone_number}")
            print(f"  Location: {vendor.location}")
        else:
            print("Vendor not found.")
    except ValueError:
        print("Please enter a valid number.")

# Find crop by ID
def find_crop():
    crop_id = input("Enter crop ID: ")
    try:
        crop = Crop.find_by_id(int(crop_id))
        if crop:
            print(f"Found crop: {crop}")
            print(f"  Season: {crop.season}")
            print(f"  Market Section: {crop.market_section}")
        else:
            print("Crop not found.")
    except ValueError:
        print("Please enter a valid number.")

# Remove vendor
def remove_vendor():
    vendor_id = input("Enter vendor ID to remove: ")
    try:
        vendor = Vendor.find_by_id(int(vendor_id))
        if vendor:
            confirm = input(f"Are you sure you want to remove {vendor.name}? (y/N): ")
            if confirm.lower() == 'y':
                vendor.delete()
                print(f"Removed vendor: {vendor.name}")
            else:
                print("Removal cancelled.")
        else:
            print("Vendor not found.")
    except ValueError:
        print("Please enter a valid number.")

# Create sale transaction
def create_sale():
    print("Create a new sale:")
    
    # Vendor
    vendor_id = input("Enter vendor ID: ")
    try:
        vendor = Vendor.find_by_id(int(vendor_id))
        if not vendor:
            print(" Vendor not found.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Crop
    crop_id = input("Enter crop ID: ")
    try:
        crop = Crop.find_by_id(int(crop_id))
        if not crop:
            print(" Crop not found.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Price and quantity
    try:
        price_per_kg = float(input("Enter price per kg (KSH): "))
        quantity_kg = float(input("Enter quantity (kg): "))
    except ValueError:
        print("Please enter valid numbers for price and quantity.")
        return
    
    market_day = input("Enter market day (optional): ")
    
    # Save sale
    sale = Sale.create(vendor, crop, price_per_kg, quantity_kg, market_day)
    total_value = price_per_kg * quantity_kg
    print(f"Sale created! Total value: KSH {total_value:.2f}")

# Show all sales
def view_sales():
    sales = Sale.get_all()
    if sales:
        print("All sales:")
        print(f"{'ID':<5} {'Vendor':<20} {'Crop':<15} {'Price/kg':<10} {'Qty':<8} {'Total':<10} {'Date':<20}")
        print("-" * 95)
        for sale in sales:
            total = sale.price_per_kg * sale.quantity_kg
            vendor_name = sale.vendor.name if sale.vendor else "Unknown"
            crop_name = sale.crop.name if sale.crop else "Unknown"
            date_str = sale.transaction_date.strftime("%Y-%m-%d %H:%M") if sale.transaction_date else "Unknown"
            print(f"{sale.id:<5} {vendor_name:<20} {crop_name:<15} {sale.price_per_kg:<10.2f} {sale.quantity_kg:<8.1f} {total:<10.2f} {date_str:<20}")
    else:
        print("No sales found.")

# Market analytics
def market_analytics():
    print("\n" + "="*80)
    print("KENYAN MARKET ANALYTICS")
    print("="*80)
    
    # Data
    vendors = Vendor.get_all()
    crops = Crop.get_all()
    sales = Sale.get_all()
    
    # Vendors by type
    vendor_types = {}
    for vendor in vendors:
        vendor_types[vendor.vendor_type] = vendor_types.get(vendor.vendor_type, 0) + 1
    
    print(f"\nVENDOR BREAKDOWN:")
    print("-" * 30)
    for vendor_type, count in vendor_types.items():
        print(f"  {vendor_type}: {count} vendors")
    
    # Crops by season
    season_crops = {}
    for crop in crops:
        season_crops[crop.season] = season_crops.get(crop.season, 0) + 1
    
    print(f"\nCROPS BY SEASON:")
    print("-" * 30)
    for season, count in season_crops.items():
        print(f"  {season}: {count} crops")
    
    # Sales summary
    if sales:
        total_sales = len(sales)
        total_value = sum(sale.price_per_kg * sale.quantity_kg for sale in sales)
        avg_price = total_value / sum(sale.quantity_kg for sale in sales) if sum(sale.quantity_kg for sale in sales) > 0 else 0
        
        print(f"\nSALES SUMMARY:")
        print("-" * 30)
        print(f"  Total sales: {total_sales}")
        print(f"  Total value: KSH {total_value:.2f}")
        print(f"  Average price per kg: KSH {avg_price:.2f}")
    
    print("\n" + "="*80)

# Show everything (tables)
def view_all_data():
    print("\n" + "="*80)
    print("KENYAN MARKET DATABASE OVERVIEW")
    print("="*80)
    
    # Vendors
    vendors = Vendor.get_all()
    print(f"\nVENDORS ({len(vendors)} records):")
    print("-" * 60)
    if vendors:
        print(f"{'ID':<5} {'Name':<20} {'Type':<12} {'Phone':<15} {'Location':<15}")
        print("-" * 70)
        for vendor in vendors:
            print(f"{vendor.id:<5} {vendor.name:<20} {vendor.vendor_type:<12} {vendor.phone_number:<15} {vendor.location:<15}")
    else:
        print("No vendors found")
    
    # Crops
    crops = Crop.get_all()
    print(f"\nCROPS ({len(crops)} records):")
    print("-" * 50)
    if crops:
        print(f"{'ID':<5} {'Name':<20} {'Season':<12} {'Section':<12}")
        print("-" * 50)
        for crop in crops:
            print(f"{crop.id:<5} {crop.name:<20} {crop.season:<12} {crop.market_section:<12}")
    else:
        print("No crops found")
    
    # Sales
    sales = Sale.get_all()
    print(f"\nSALES ({len(sales)} records):")
    print("-" * 70)
    if sales:
        print(f"{'ID':<5} {'Vendor':<20} {'Crop':<15} {'Price/kg':<10} {'Qty':<8} {'Market Day':<12}")
        print("-" * 75)
        for sale in sales:
            vendor_name = sale.vendor.name if sale.vendor else "Unknown"
            crop_name = sale.crop.name if sale.crop else "Unknown"
            print(f"{sale.id:<5} {vendor_name:<20} {crop_name:<15} {sale.price_per_kg:<10.2f} {sale.quantity_kg:<8.1f} {sale.market_day:<12}")
    else:
        print("No sales found")
    
    # Market requests
    requests = MarketRequest.get_all()
    print(f"\nMARKET REQUESTS ({len(requests)} active):")
    print("-" * 80)
    if requests:
        print(f"{'ID':<5} {'Buyer':<20} {'Wanting':<15} {'Quantity':<10} {'Max Price/kg':<12} {'Date':<15}")
        print("-" * 85)
        for req in requests:
            date_str = req.request_date.strftime("%Y-%m-%d") if req.request_date else "Unknown"
            print(f"{req.id:<5} {req.vendor_name:<20} {req.crop_name:<15} {req.quantity_kg:<10.1f} {req.max_price_per_kg:<12.2f} {date_str:<15}")
    else:
        print("No active requests found")
    
    print("\n" + "="*80)

# Create market buying request
def create_market_request():
    print("\n=== CREATE BUYING REQUEST ===")
    
    # Vendors
    vendors = Vendor.get_all()
    if not vendors:
        print("No vendors available. Please add vendors first.")
        return
    
    print("Available vendors:")
    for vendor in vendors:
        print(f"{vendor.id}. {vendor.name} ({vendor.vendor_type})")
    
    try:
        vendor_id = int(input("Enter vendor ID (who wants to buy): "))
        vendor = Vendor.find_by_id(vendor_id)
        if not vendor:
            print("Invalid vendor ID!")
            return
    except ValueError:
        print("Invalid vendor ID!")
        return
    
    crop_name = input("Enter crop name they want to buy: ")
    
    try:
        quantity_kg = float(input("Enter quantity needed (kg): "))
        if quantity_kg <= 0:
            print("Quantity must be positive!")
            return
    except ValueError:
        print("Invalid quantity!")
        return
    
    try:
        max_price_per_kg = float(input("Enter maximum price willing to pay per kg (KSH): "))
        if max_price_per_kg <= 0:
            print("Price must be positive!")
            return
    except ValueError:
        print("Invalid price!")
        return
    
    contact_info = input("Enter contact info (phone/location): ")
    
    # Save request
    request = MarketRequest.create(
        vendor_id=vendor.id,
        vendor_name=vendor.name,
        crop_name=crop_name,
        quantity_kg=quantity_kg,
        max_price_per_kg=max_price_per_kg,
        contact_info=contact_info
    )
    
    print(f"\n Market request created successfully!")
    print(f"   Buyer: {vendor.name}")
    print(f"   Wanting: {crop_name}")
    print(f"   Quantity: {quantity_kg} kg")
    print(f"   Max Price: KSH {max_price_per_kg}/kg")
    print(f"   Contact: {contact_info}")

# Show market requests
def view_market_requests():
    requests = MarketRequest.get_all()
    if requests:
        print("\nACTIVE MARKET REQUESTS (Buying Opportunities):")
        print("="*85)
        print(f"{'ID':<5} {'Buyer':<20} {'Wanting':<15} {'Quantity':<10} {'Max Price/kg':<12} {'Date':<15} {'Contact':<15}")
        print("-" * 95)
        for req in requests:
            date_str = req.request_date.strftime("%Y-%m-%d") if req.request_date else "Unknown"
            contact = req.contact_info if req.contact_info else "N/A"
            print(f"{req.id:<5} {req.vendor_name:<20} {req.crop_name:<15} {req.quantity_kg:<10.1f} {req.max_price_per_kg:<12.2f} {date_str:<15} {contact:<15}")
        
        print(f"\n Total active requests: {len(requests)}")
        print(" Farmers can check this list to find buyers for their produce!")
    else:
        print("No active market requests found.")

# Remove market request
def remove_market_request():
    requests = MarketRequest.get_all()
    if not requests:
        print("No active market requests found.")
        return
    
    print("Active requests:")
    for req in requests:
        print(f"{req.id}. {req.vendor_name} wants {req.crop_name}")
    
    try:
        request_id = int(input("Enter request ID to remove: "))
        request = MarketRequest.find_by_id(request_id)
        if request:
            confirm = input(f"Are you sure you want to remove request {request_id}? (y/n): ")
            if confirm.lower() == 'y':
                request.delete()
                print("Request removed successfully!")
            else:
                print("Request removal cancelled.")
        else:
            print("Request not found!")
    except ValueError:
        print("Invalid request ID!")
