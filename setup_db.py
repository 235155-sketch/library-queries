import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);
INSERT INTO books VALUES
(1, 'Data Science Basics', 'Technology', 1450, 10),
(2, 'Clean Code', 'Technology', 1200, 6),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'The Alchemist', 'Fiction', 800, 3),
(5, 'Atomic Habits', 'Self-Help', 950, 12),
(6, '1984', 'Fiction', 700, 4),
(7, 'Python Crash Course', 'Technology', 1100, 8),
(8, 'Sapiens', 'History', 1250, 7);
""")

conn.commit()
conn.close()
print("Database created.")
