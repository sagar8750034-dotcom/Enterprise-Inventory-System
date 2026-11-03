import unittest

from models import Book, Magazine, DigitalMedia
from inventory import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inventory= InventoryManager()
        self.book = Book("B1", "Python Basics", 500, "A. Kumar")

    def test_add_item(self):
        result = self.inventory.add_item(self.book)

        self.assertIn("Added: ", result)
        self.assertIn("B1", self.inventory.items)

    def test_duplicate_items(self):
        self.inventory.add_item(self.book)

        with self.assertRaises(ValueError):
         self.inventory.add_item(self.book)

    def test_checkout_item(self):
       self.inventory.add_item(self.book)

       result = self.inventory.checkout_item("B1")

       self.assertIn("Checked out", result)
       self.assertIn("B1", self.inventory.checked_out)

    def test_checkout_missing_item(self):
       with self.assertRaises(KeyError):
          self.inventory.checkout_item("X1")

    def test_audit_report(self):
       self.inventory.add_item(self.book)

       report = self.inventory.generate_audit_report()

       self.assertEqual(len(report), 1)
       self.assertEqual(report[0]["Status"], "Available")
       self.assertEqual(report[0]["Fee"], 25.0)

if __name__ == "__main__":
   unittest.main()