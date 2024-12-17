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

# Create the products table
def create_products_table():
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                product_type TEXT NOT NULL,
                price REAL NOT NULL,
                farmer_id INTEGER,
                FOREIGN KEY (farmer_id) REFERENCES farmers(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        print("Products table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

# Add a product to the database
def add_product(name, product_type, price, farmer_id):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (name, product_type, price, farmer_id)
            VALUES (?, ?, ?, ?)
        """, (name, product_type, price, farmer_id))
        conn.commit()
        print("Product added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        conn.close()

# View all products
def view_products():
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products
    except sqlite3.Error as e:
        print(f"Error fetching products: {e}")
        return []
    finally:
        conn.close()

# Update a product
def update_product(product_id, name, product_type, price, farmer_id):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products
            SET name = ?, product_type = ?, price = ?, farmer_id = ?
            WHERE id = ?
        """, (name, product_type, price, farmer_id, product_id))
        conn.commit()
        print("Product updated successfully!")
    except sqlite3.Error as e:
        print(f"Error updating product: {e}")
    finally:
        conn.close()

# Delete a product
def delete_product(product_id):
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        print("Product deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting product: {e}")
    finally:
        conn.close()
