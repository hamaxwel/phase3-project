import sqlite3

# Database file path
DATABASE_FILE = "farm_management.db"

# Establish a database connection
def connect_db():
    try:
        return sqlite3.connect(DATABASE_FILE)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Initialize the database and create necessary tables
def init_db():
    conn = connect_db()
    if conn is None:  # Check if the connection failed
        print("Failed to connect to the database. Exiting initialization.")
        return

    try:
        cursor = conn.cursor()

        # Create 'farmers' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS farmers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """)

        # Create 'products' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                product_type TEXT NOT NULL,
                price REAL NOT NULL,
                farmer_id INTEGER NOT NULL,
                FOREIGN KEY(farmer_id) REFERENCES farmers(id) ON DELETE CASCADE
            )
        """)

        # Create 'sales' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity_sold INTEGER NOT NULL,
                sale_date TEXT NOT NULL,
                customer_name TEXT NOT NULL,
                customer_contact TEXT NOT NULL,
                FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
            )
        """)

        conn.commit()  # Commit changes to the database
        print("Database and tables initialized successfully!")
    except sqlite3.Error as e:
        print(f"Error initializing tables: {e}")
    finally:
        conn.close()  # Ensure the connection is closed

# Example to insert sample data into the tables (for testing purposes)
def add_sample_data():
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()

        # Insert sample farmers
        cursor.execute("INSERT INTO farmers (name, email, phone, location) VALUES (?, ?, ?, ?)", 
                       ("John Doe", "john@example.com", "123-456-7890", "Kenya"))
        cursor.execute("INSERT INTO farmers (name, email, phone, location) VALUES (?, ?, ?, ?)", 
                       ("Jane Smith", "jane@example.com", "987-654-3210", "Tanzania"))
        conn.commit()

        # Get farmer ids (for products)
        cursor.execute("SELECT id FROM farmers WHERE email = 'john@example.com'")
        farmer_id_john = cursor.fetchone()[0]
        cursor.execute("SELECT id FROM farmers WHERE email = 'jane@example.com'")
        farmer_id_jane = cursor.fetchone()[0]

        # Insert sample products
        cursor.execute("INSERT INTO products (name, product_type, price, farmer_id) VALUES (?, ?, ?, ?)", 
                       ("Tomatoes", "Vegetable", 5.0, farmer_id_john))
        cursor.execute("INSERT INTO products (name, product_type, price, farmer_id) VALUES (?, ?, ?, ?)", 
                       ("Onions", "Vegetable", 3.0, farmer_id_jane))
        conn.commit()

        # Get product ids (for sales)
        cursor.execute("SELECT id FROM products WHERE name = 'Tomatoes'")
        product_id_tomatoes = cursor.fetchone()[0]
        cursor.execute("SELECT id FROM products WHERE name = 'Onions'")
        product_id_onions = cursor.fetchone()[0]

        # Insert sample sales
        cursor.execute("INSERT INTO sales (product_id, quantity_sold, sale_date, customer_name, customer_contact) VALUES (?, ?, ?, ?, ?)", 
                       (product_id_tomatoes, 10, "2024-12-17", "Alice Brown", "555-1234"))
        cursor.execute("INSERT INTO sales (product_id, quantity_sold, sale_date, customer_name, customer_contact) VALUES (?, ?, ?, ?, ?)", 
                       (product_id_onions, 5, "2024-12-17", "Bob White", "555-5678"))
        conn.commit()
        
        print("Sample data added successfully!")

    except sqlite3.Error as e:
        print(f"Error adding sample data: {e}")
    finally:
        conn.close()  # Ensure the connection is closed

# # Entry point for testing table creation and adding sample data
# if __name__ == "__main__":
#     init_db()  # Initialize database and tables
#     add_sample_data()  # Add sample data to test
