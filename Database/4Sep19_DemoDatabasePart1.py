# 1. Connect to the database
# 2. Create a Cursor Object
# 3. Write an SQL Query
#  4. Commit the changes
# 5. Close Connection

import sqlite3

import sqlite3

def CreateTable():
    conn = sqlite3.Connection('dblite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def Insert(item, quantity, price):
    conn = sqlite3.Connection('dblite.db')
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('Sample', 14, 44.00)")
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.Connection('dblite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchone()
    conn.close()
    return rows

def Delete(item):
    conn = sqlite3.Connection('dblite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def UPDATE(quantity, price, item):
    conn = sqlite3.Connection('dblite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item=?", (quantity, price,item))
    conn.commit()
    conn.close()

# Insert('Tea', 20, 15.32)

Delete('Sample')
# UPDATE(20,200.2,'Tea')
row = view()
print(row)
# print(view())

