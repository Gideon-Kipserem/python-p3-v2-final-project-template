# lib/cli.py

from helpers import (
    exit_program,
    add_vendor,
    view_vendors,
    add_crop,
    view_crops,
    find_vendor,
    find_crop,
    remove_vendor,
    create_sale,
    view_sales,
    market_analytics,
    view_all_data,
    create_market_request,
    view_market_requests,
    remove_market_request
)

# Main entry point
def main():
    print("Karibu! Welcome to the Kenyan Market Management System!")
    print("Manage vendors, crops, and track sales in your fresh produce market.")
    print()

    # Loop for user menu
    while True:
        menu()
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_vendor()
        elif choice == "2":
            view_vendors()
        elif choice == "3":
            add_crop()
        elif choice == "4":
            view_crops()
        elif choice == "5":
            find_vendor()
        elif choice == "6":
            find_crop()
        elif choice == "7":
            remove_vendor()
        elif choice == "8":
            create_sale()
        elif choice == "9":
            view_sales()
        elif choice == "10":
            market_analytics()
        elif choice == "11":
            view_all_data()
        elif choice == "12":
            create_market_request()
        elif choice == "13":
            view_market_requests()
        elif choice == "14":
            remove_market_request()
        else:
            print("Invalid choice")

# Menu text
def menu():
    print("\n" + "="*80)
    print("KENYAN MARKET MANAGEMENT SYSTEM")
    print("="*80)
    print("1.  Add a vendor")
    print("2.  View all vendors")
    print("3.  Add a crop")
    print("4.  View all crops")
    print("5.  Find a vendor")
    print("6.  Find a crop")
    print("7.  Remove a vendor")
    print("8.  Create a sale")
    print("9.  View all sales")
    print("10. Market analytics")
    print("11. View all data in tables")
    print("12. Create buying request")
    print("13. View market requests")
    print("14. Remove market request")
    print("0.  Exit the program")
    print("="*80)

# Run program
if __name__ == "__main__":
    main()
