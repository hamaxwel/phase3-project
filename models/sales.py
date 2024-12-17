import sqlite3

# Database file (SQLite will store the database in this file)
DATABASE_FILE = "farm_management.db"

# Connect to the SQLite database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Create the sales table
def create_sales_table():
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                quantity_sold INTEGER,
                sale_date TEXT,
                customer_name TEXT,
                customer_contact TEXT,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        print("Sales table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

# Add a sale
def add_sale(product_id, quantity_sold, sale_date, customer_name, customer_contact):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sales (product_id, quantity_sold, sale_date, customer_name, customer_contact)
            VALUES (?, ?, ?, ?, ?)
        """, (product_id, quantity_sold, sale_date, customer_name, customer_contact))
        conn.commit()
        print("Sale added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding sale: {e}")
    finally:
        conn.close()

# View all sales
def view_sales():
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()
        return sales
    except sqlite3.Error as e:
        print(f"Error fetching sales: {e}")
        return []
    finally:
        conn.close()

# Update a sale
def update_sale(sale_id):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales WHERE id = ?", (sale_id,))
        sale = cursor.fetchone()

        if sale is None:
            print(f"No sale found with ID {sale_id}.")
            return

        # Collect updated details from the user
        quantity_sold = input(f"Enter new quantity sold (current: {sale[2]}): ") or sale[2]
        quantity_sold = int(quantity_sold)
        sale_date = input(f"Enter new sale date (current: {sale[3]}): ") or sale[3]
        customer_name = input(f"Enter new customer name (current: {sale[4]}): ") or sale[4]
        customer_contact = input(f"Enter new customer contact (current: {sale[5]}): ") or sale[5]

        # Update the sale's details in the database
        cursor.execute("""
            UPDATE sales
            SET quantity_sold = ?, sale_date = ?, customer_name = ?, customer_contact = ?
            WHERE id = ?
        """, (quantity_sold, sale_date, customer_name, customer_contact, sale_id))
        conn.commit()
        print(f"Sale with ID {sale_id} updated successfully!")
    except sqlite3.Error as e:
        print(f"Error updating sale: {e}")
    finally:
        conn.close()

# Delete a sale
def delete_sale(sale_id):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sales WHERE id = ?", (sale_id,))
        conn.commit()
        print(f"Sale with ID {sale_id} deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting sale: {e}")
    finally:
        conn.close()
