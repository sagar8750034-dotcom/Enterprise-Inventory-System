from datetime import date
from models import Item

class InventoryManager:
    """Manage inventory items, checkout, returns, and audit reports."""

    def __init__(self):
        self.items = {}
        self.checked_out = {}

    def add_item(self, item):
        if not isinstance(item,Item):
            raise TypeError("Only Item objects can be added.")

        if item.item_id in self.items:
            raise ValueError(f"Item ID {item.item_id} already exists. ")

        self.items[item.item_id] = item
        return f"Added: {item}"

    def get_item(self, item_id):
        return self.items.get(item_id)

    def checkout_item(self, item_id):
        if item_id not in self.items:
            raise KeyError(f"Item ID {item_id} not found.")

        if item_id in self.checked_out:
            raise ValueError(f"Item {item_id} is already checked out.")

        item = self.items[item_id]
        self.checked_out[item_id] = date.today().isoformat()

        if hasattr(item, "borrow_date"):
            item.borrow_date = self.checked_out[item_id]

        return f"Checked out: {item}"

    def return_item(self, item_id):
        if item_id not in self.checked_out:
            raise ValueError(f"Item {item_id} is not checked out.")

        item = self.items[item_id]
        checkout_date = self.checked_out.pop(item_id)

        if hasattr(item, "borrow_date"):
            item.borrow_date = None

        return f"Returned: {item} (checked out on {checkout_date})"

    def generate_audit_report(self):
        report = []

        for item_id, item in self.items.items():
            metadata = item.display_metadata()
            metadata["Status"] = (
                "Checked Out" if item_id in self.checked_out else "Available"
            )
            metadata["Fee"] = item.calculate_fee()
            report.append(metadata)

        return report