# Farm Management System
=====================================

## Overview
------------

This is a simple Farm Management System built using Python and SQLite, which allows farmers to manage their products, sales, and personal information in a structured database. The system includes CRUD operations for farmers, products, and sales, providing an easy-to-use interface for maintaining farm data.

## Features
------------

*   Farmer Management: Add, view, update, and delete farmer details.
*   Product Management: Add, view, update, and delete products related to the farm.
*   Sales Management: Add, view, update, and delete sales transactions.
*   SQLite Database: Uses SQLite to persist data for farmers, products, and sales.

## Prerequisites
-----------------

*   Python 3.x
*   SQLite3 (SQLite is included with Python by default)

## Installation
--------------

### Clone the Repository

```bash
git clone https://github.com/your-username/farm-management-system.git
```

### Navigate to the Project Directory

```bash
cd farm-management-system
```

### Check Python Version

```bash
python --version
```

No external libraries are required as SQLite is included with Python.

## Usage
-----

### Run the Main Program

```bash
python main.py
```

You will be presented with the following options:

*   Add Farmer: Add a new farmer to the system.
*   View Farmers: View a list of all farmers.
*   Delete Farmer: Delete a farmer by ID.
*   Update Farmer: Update farmer details by ID.
*   Add Product: Add a new product related to the farm.
*   View Products: View a list of all products.
*   Update Product: Update product details by ID.
*   Delete Product: Delete a product by ID.
*   Add Sale: Add a new sale transaction.
*   View Sales: View a list of all sales transactions.
*   Update Sale: Update sale transaction details by ID.
*   Delete Sale: Delete a sale transaction by ID.
*   Exit: Exit the application.

Follow the prompts in the terminal to interact with the system.

## Database Structure
---------------------

The system uses a SQLite database to store the following tables:

*   farmers: Stores farmer information (ID, name, email, phone, location).
*   products: Stores product information (ID, name, product type, price, farmer ID).
*   sales: Stores sales transaction details (ID, product ID, quantity sold, sale date, customer name, customer contact).

The database file `farm_management.db` is automatically created in the project directory when you run the program.

## Example Workflow
-------------------

### Add Farmer

*   Enter farmer's name, email, phone, and location.

### Add Product

*   Select a farmer from the system and enter product details (name, type, price).

### Add Sale

*   Enter the product ID, quantity sold, sale date, customer name, and customer contact information.

### Update Product/Farmer/Sale

*   Select the ID of the item (product/farmer/sale) to update, then modify the fields as needed.

## Contributing
------------

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Contributions are always welcome!

### Fork the Repository

### Create a New Branch

```bash
git checkout -b feature-name
```

### Make Your Changes

### Commit Your Changes

```bash
git commit -am 'Add feature'
```

### Push to the Branch

```bash
git push origin feature-name
```

### Create a New Pull Request

## License
-------

This project is licensed under the MIT License - see the LICENSE file for details.