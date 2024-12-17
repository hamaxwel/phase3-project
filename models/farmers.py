import sqlite3

# Function to create the farmers table
def create_farmers_table():
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_farmer():
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    name = input("Enter farmer's name: ")
    email = input("Enter farmer's email: ")
    phone = input("Enter farmer's phone: ")
    location = input("Enter farmer's location: ")

    query = "INSERT INTO farmers (name, email, phone, location) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, email, phone, location))
    conn.commit()

    print("Farmer added successfully!\n")
    cursor.close()
    conn.close()

def view_farmers():
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    query = "SELECT * FROM farmers"
    cursor.execute(query)
    farmers = cursor.fetchall()

    if not farmers:
        print("No farmers found.\n")
    else:
        print("Farmers List:")
        for farmer in farmers:
            print(f"ID: {farmer[0]}, Name: {farmer[1]}, Email: {farmer[2]}, Phone: {farmer[3]}, Location: {farmer[4]}")
    print()
    cursor.close()
    conn.close()

def delete_farmer():
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    farmer_id = int(input("Enter farmer ID to delete: "))
    query = "DELETE FROM farmers WHERE id = ?"
    cursor.execute(query, (farmer_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Farmer not found.\n")
    else:
        print("Farmer deleted successfully!\n")
    cursor.close()
    conn.close()

# Function to update farmer details
def update_farmer():
    conn = sqlite3.connect("farm_management.db")
    cursor = conn.cursor()

    # Get the farmer ID to update
    farmer_id = int(input("Enter farmer ID to update: "))
    
    # Fetch the current data of the farmer
    query = "SELECT * FROM farmers WHERE id = ?"
    cursor.execute(query, (farmer_id,))
    farmer = cursor.fetchone()

    if farmer is None:
        print("Farmer not found.\n")
        cursor.close()
        conn.close()
        return

    # Show current details of the farmer
    print(f"Current Details: Name: {farmer[1]}, Email: {farmer[2]}, Phone: {farmer[3]}, Location: {farmer[4]}")

    # Get new details from the user, retain current data if input is empty
    name = input(f"Enter new name (leave blank to keep '{farmer[1]}'): ") or farmer[1]
    email = input(f"Enter new email (leave blank to keep '{farmer[2]}'): ") or farmer[2]
    phone = input(f"Enter new phone (leave blank to keep '{farmer[3]}'): ") or farmer[3]
    location = input(f"Enter new location (leave blank to keep '{farmer[4]}'): ") or farmer[4]

    # Update the farmer data in the database
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
