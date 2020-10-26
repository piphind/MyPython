import sqlite3


def create_table():
    # Create and connect
    conn = sqlite3.connect("lite.db")
    # Create a cursor
    cur = conn.cursor()
    # Create a table (if it doesn't already exist)
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(f_item, f_quantity, f_price):
    # Create and connect
    conn = sqlite3.connect("lite.db")
    # Create a cursor
    cur = conn.cursor()
    # Add some data
    cur.execute("INSERT INTO store VALUES (?,?,?)", (f_item, f_quantity, f_price))
    # Commit the changes
    conn.commit()
    # Close the connection to the database
    conn.close()


def view():
    # Create and connect
    conn = sqlite3.connect("lite.db")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(f_item):
    # Create and connect
    conn = sqlite3.connect("lite.db")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("DELETE FROM store WHERE item=?", (f_item,))
    conn.commit()
    conn.close()


def update(f_item, f_quantity):
    # Create and connect
    conn = sqlite3.connect("lite.db")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("UPDATE store SET quantity=? WHERE item=?", (f_quantity, f_item))
    conn.commit()
    conn.close()


print("Stage 1 - Initial view:")
print(view())
insert("Coffee Cup", 3, 12.99)
print("Stage 2 - Record Inserted:")
print(view())
delete("Coffee Cup")
print("Stage 3 - Record Deleted:")
print(view())
update("Wine Glass", 15)
print("Stage 4 - Quantity Updated:")
print(view())
