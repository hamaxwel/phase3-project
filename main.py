from models.products import *
from models.sales import *
from models.farmers import *

def main_menu():
    # Initialize tables
    create_farmers_table()
    create_products_table()
    create_sales_table()

    while True:
        print("==== Farm Management System ====")
        print("1. Add Farmer")
        print("2. View Farmers")
        print("3. Delete Farmer")
        print("4. Update Farmer")
        print("5. Add Product")
        print("6. View Products")
        print("7. Update Product")
        print("8. Delete Product")
        print("9. Add Sale")
        print("10. View Sales")
        print("11. Update Sale")
        print("12. Delete Sale")
        print("13. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_farmer()
        elif choice == "2":
            view_farmers()
        elif choice == "3":
            farmer_id = int(input("Enter farmer ID to delete: "))
            delete_farmer(farmer_id)
        elif choice == "4":
            farmer_id = int(input("Enter farmer ID to update: "))
            update_farmer(farmer_id)
        elif choice == "5":
            name = input("Enter product name: ")
            product_type = input("Enter product type: ")
            price = float(input("Enter product price: "))
            farmer_id = int(input("Enter farmer ID: "))
            add_product(name, product_type, price, farmer_id)
        elif choice == "6":
            view_products()
        elif choice == "7":
            product_id = int(input("Enter product ID to update: "))
            update_product(product_id)
        elif choice == "8":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == "9":
            product_id = int(input("Enter product ID: "))
            quantity_sold = int(input("Enter quantity sold: "))
            sale_date = input("Enter sale date (YYYY-MM-DD): ")
            customer_name = input("Enter customer name: ")
            customer_contact = input("Enter customer contact: ")
            add_sale(product_id, quantity_sold, sale_date, customer_name, customer_contact)
        elif choice == "10":
            view_sales()
        elif choice == "11":
            sale_id = int(input("Enter sale ID to update: "))
            update_sale(sale_id)
        elif choice == "12":
            sale_id = int(input("Enter sale ID to delete: "))
            delete_sale(sale_id)
        elif choice == "13":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Function to update a product
def update_product(product_id):
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    # Fetch the current product details
    query = "SELECT * FROM products WHERE id = ?"
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    if product is None:
        print("Product not found.\n")
        cursor.close()
        conn.close()
        return

    # Display current product details
    print(f"Current Details: Name: {product[1]}, Type: {product[2]}, Price: {product[3]}, Farmer ID: {product[4]}")

    # Ask for new details
    name = input(f"Enter new name (leave blank to keep '{product[1]}'): ") or product[1]
    product_type = input(f"Enter new type (leave blank to keep '{product[2]}'): ") or product[2]
    price = input(f"Enter new price (leave blank to keep '{product[3]}'): ")
    price = float(price) if price else product[3]
    farmer_id = input(f"Enter new farmer ID (leave blank to keep '{product[4]}'): ")
    farmer_id = int(farmer_id) if farmer_id else product[4]

    # Update the product
    query = """
    UPDATE products
    SET name = ?, product_type = ?, price = ?, farmer_id = ?
    WHERE id = ?
    """
    cursor.execute(query, (name, product_type, price, farmer_id, product_id))
    conn.commit()

    print("Product updated successfully!\n")
    cursor.close()
    conn.close()

# Function to update a farmer
def update_farmer(farmer_id):
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    # Fetch the current farmer details
    query = "SELECT * FROM farmers WHERE id = ?"
    cursor.execute(query, (farmer_id,))
    farmer = cursor.fetchone()

    if farmer is None:
        print("Farmer not found.\n")
        cursor.close()
        conn.close()
        return

    # Display current farmer details
    print(f"Current Details: Name: {farmer[1]}, Email: {farmer[2]}, Phone: {farmer[3]}, Location: {farmer[4]}")

    # Ask for new details
    name = input(f"Enter new name (leave blank to keep '{farmer[1]}'): ") or farmer[1]
    email = input(f"Enter new email (leave blank to keep '{farmer[2]}'): ") or farmer[2]
    phone = input(f"Enter new phone (leave blank to keep '{farmer[3]}'): ") or farmer[3]
    location = input(f"Enter new location (leave blank to keep '{farmer[4]}'): ") or farmer[4]

    # Update the farmer
    query = """
    UPDATE farmers
    SET name = ?, email = ?, phone = ?, location = ?
    WHERE id = ?
    """
    cursor.execute(query, (name, email, phone, location, farmer_id))
    conn.commit()

    print("Farmer details updated successfully!\n")
    cursor.close()
    conn.close()

# Run the program
if __name__ == "__main__":
    main_menu()
