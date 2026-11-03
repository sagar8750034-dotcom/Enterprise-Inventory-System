# Ēnterprise Smart Inventory & Asset System
 
A Python-based inventory management system built using object-oriented Prograumming (OOP)principles.  It allows users to manage books, magazines, and digital media through an interactive terminal interface.

## Features

##Features

- Add Books, Magazines, and Digital Media.
- View all  inventory items.
- Search items using unique item IDs.
- Checkout and return inventory items.
- Generate inventory audit reports.
- Calculate applicable fees for different item types.
- Prevent duplicate item IDs.
- Validate item prices and user inputs.
- Track item availability status.

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Abstract Base Classes (ABC)
- Inheritance and Poymorphism
- Encapsulation and Properties
- Python Unittest Framework

## Project Structure
Enterprise-Inventory-System/
│
├── models.py
├── inventory.py
├── test_inventory.py
├── main.py
├── README.md
└── .gitignore

## OOP Concept Implemented

- **Abstraction:** Uses an abstract Item class with abstract methods.
- **Inheritance:** Book, Magazine, and DigitalMedia inherit from Item.
- **Encapsulation:** Uses properties to control access to item prices.
- **Polymorphism** Different item types implement their own fee calculation and metadata methods.

## Installation

1. Clone the repositiory:
   git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory:
   cd Enterprise-Inventory-System

3. Run the application:
   python main.py

## How to Run Tests
Execute the following command:   

python -m unittest test_inventory -v

## Applicable Menu

1. Add Book
2. Add Magazine
3. Add Digital Media
4. View All Items
5. Search Item
6. Checkout Item
7. Return Item
8. Generate Audit Report
9. Exit

## Future Improvement
- Store inventory data in a database.
- Add a graphical user interface.
- Implement user authentication.
- Export audit reports to CSV.
- Build REST APIs using FastAPI.

## Author

Sagar Singh