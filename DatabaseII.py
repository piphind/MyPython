import psycopg2


def create_table():
    # Create and connect
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='genesis' host='localhost' port='5432'")
    # Create a cursor
    cur = conn.cursor()
    # Create a table (if it doesn't already exist)
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(f_item, f_quantity, f_price):
    # Create and connect
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='genesis' host='localhost' port='5432'")
    # Create a cursor
    cur = conn.cursor()
    # Add some data
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (f_item, f_quantity, f_price))
    # Commit the changes
    conn.commit()
    # Close the connection to the database
    conn.close()


def view():
    # Create and connect
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='genesis' host='localhost' port='5432'")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(f_item):
    # Create and connect
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='genesis' host='localhost' port='5432'")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("DELETE FROM store WHERE item=%s", (f_item,))
    conn.commit()
    conn.close()


def update(f_item, f_quantity):
    # Create and connect
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='genesis' host='localhost' port='5432'")
    # Create a cursor
    cur = conn.cursor()
    # Retrieve the data
    cur.execute("UPDATE store SET quantity=%s WHERE item=%s", (f_quantity, f_item))
    conn.commit()
    conn.close()


# insert("Melon", 8, 3.75)
# print("Stage 1 - Initial view:")
# print(view())
# insert("Coffee Cup", 3, 12.99)
# print("Stage 2 - Record Inserted:")
# print(view())
delete("Melon")
# print("Stage 3 - Record Deleted:")
# print(view())
# update("Melon", 2)
# print("Stage 4 - Quantity Updated:")
print(view())
