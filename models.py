from abc import ABC, abstractmethod


class Item(ABC):
    """Abstract base class for inventory items."""

    def __init__(self, item_id, title, price):
        self.item_id = item_id
        self.title = title
        self._price = 0
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @abstractmethod
    def calculate_fee(self):
        """Calculate the applicable fee for an item."""
        pass

    @abstractmethod
    def display_metadata(self):
        """Return item details."""
        pass

    def __str__(self):
        return f"{self.title} (ID: {self.item_id})"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"item_id={self.item_id!r}, title={self.title!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.item_id == other.item_id

class Book(Item):
    def __init__(self, item_id, title, price, author, borrow_date=None):
        super().__init__(item_id, title, price)
        self.author = author
        self._borrow_date = borrow_date

    @property
    def borrow_date(self):
        return self._borrow_date

    @borrow_date.setter
    def borrow_date(self, value):
        self._borrow_date = value

    def calculate_fee(self):
        return round(self.price * 0.05, 2)

    def display_metadata(self):
        return {
            "ID" : self.item_id,
            "Type" : "Book",
            "Title" : self.title,
            "Author" : self.author,
            "Price" : self.price,
            "Borrow Date" : self.borrow_date,
        }

class Magazine(Item):
    def __init__(self, item_id, title, price, issue_number):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number

    def calculate_fee(self):
        return round(self.price * 0.02, 2)

    def display_metadata(self):
        return {
            "ID" : self.item_id,
            "Type" : "Magazine",
            "Title" : self.title,
            "Issue Number" : self.issue_number,
            "Price" : self.price,
        }

class DigitalMedia(Item):
    def __init__(self, item_id, title, price, file_format):
        super().__init__(item_id, title, price)
        self.file_format = file_format

    def calculate_fee(self):
        return 0.0

    def display_metadata(self):
        return {
            "ID" : self.item_id,
            "Type" : "Digital Media",
            "Title" : self.title,
            "Format" : self.file_format,
            "Price" : self.price,
        }