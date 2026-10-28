import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# (a) Price > 1000, sorted by price high to low
print("Books above Rs.1000 (sorted):")
cur.execute("SELECT title, price FROM books WHERE price > 1000 ORDER BY price DESC;")
for row in cur.fetchall():
    print(row)

# (b) Rename title as book_title using AS
print("\nBooks with renamed column:")
cur.execute("SELECT title AS book_title, price FROM books;")
for row in cur.fetchall():
    print(row)

# (c) Fiction books with stock < 5 (low-stock alert)
print("\nLow-stock Fiction books:")
cur.execute("SELECT title, genre, price, stock FROM books WHERE genre = 'Fiction' AND stock < 5;")
for row in cur.fetchall():
    print(row)

conn.close()
