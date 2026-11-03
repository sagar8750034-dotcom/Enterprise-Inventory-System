from models import Book, Magazine, DigitalMedia
from inventory import InventoryManager

def display_menu():
    print("\n========== ENTERPRISES INVENTORY SYSTEM ==========")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Add Digital Media")
    print("4. View All Items")
    print("5. Search Item")
    print("6. Checkout Item")
    print("7. Return Item")
    print("8. Generate Audit Report")
    print("9. Exit")
    print("===================================================")

def add_item(inventory, item_type):
    try:
        item_id = input("Enter Item ID:").strip()
        title = input("Enter Title:").strip()
        price = float(input("Enter Price: "))

        if not item_id or not title:
            print("ID and Title cannot be empty.")
            return
        
        if item_type == "book":
            author = input("Enter Author name: ").strip()
            item = Book(item_id, title, price, author)

        elif item_type == "magazine":
            issue_number = input("Enter Issue Number:").strip()
            item = Magazine(item_id, title, price, issue_number)

        elif item_type == "digital":
            file_format = input("Enter File Format:").strip()
            item = DigitalMedia(item_id, title, price, file_format)

        inventory.add_item(item)
        print("Item added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")

    except Exception as error:
        print(f"Error: {error}")

def view_items(inventory):
    items = inventory.items

    if not items:
        print("Inventory is empty.")
        return

    print("\n========== Inventory Items ==========")

    for item_id, item in items.items():
        print("------------------------------------")

        for key, value in item.display_metadata().items():
            print(f"{key}: {value}")

        status = (
            "Checked Out"
            if item_id in inventory.checked_out
            else "Available"
        )
        print(f"Status: {status}")
        print(f"Applicable Fee: {item.calculate_fee()}")

def search_item(inventory):
    item_id = input("Enter Item ID to search:").strip()
    item = inventory.get_item(item_id)

    if item:
        print("\nItem Found:")
        for key, value in item.display_metadata().items():
            print(f"{key}: {value}")
    else:
        print("Item not found.")

def checkout_item(inventory):
    item_id = input("Enter Item ID to checkout:").strip()

    try:
        inventory.checkout_item(item_id)
        print("Item checked out successfully!")

    except(ValueError, KeyError) as error:
        print(f"Checkout failed: {error}")

def return_item(inventory):
    item_id = input("Enter Item ID to return: ").strip()

    try:
        inventory.return_item(item_id)
        print("Item returned successfully!")

    except (ValueError, KeyError) as error:
        print(f"Return failed: {error}")

def generate_audit_report(inventory):
    report = inventory.generate_audit_report()

    print("\n========== Audit Report ==========")
    print(report)

def main():
    inventory = InventoryManager()

    while True:
        display_menu()

        choice = input("Enter your choice(1-9): ").strip()

        if choice == "1":
            add_item(inventory, "book")

        elif choice == "2":
            add_item(inventory, "magazine")

        elif choice == "3":
            add_item(inventory, "digital")

        elif choice == "4":
            view_items(inventory)

        elif choice == "5":
            search_item(inventory)

        elif choice =="6":
            checkout_item(inventory)

        elif choice == "7":
            return_item(inventory)

        elif choice =="8":
            generate_audit_report(inventory)

        elif choice == "9":
            print("Thank you for using Enterprises Inventory System!")
            break

        else:
            print("Invalid choice. Please select between 1 and 9.")
            break
if __name__ == "__main__":
    main()