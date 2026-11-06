-- Task 2 - SQL (Library Database)
-- A simple library database with a books table, 8 records, and the
-- required queries. Written for SQLite (also works on most SQL engines).

-- 1) Create the books table
CREATE TABLE books (
    id      INTEGER PRIMARY KEY,
    title   TEXT    NOT NULL,
    author  TEXT    NOT NULL,
    price   REAL    NOT NULL
);

-- 2) Insert 8 records
INSERT INTO books (id, title, author, price) VALUES
    (1, 'The Pragmatic Programmer',      'Andrew Hunt',       650.00),
    (2, 'Clean Code',                    'Robert C. Martin',  480.00),
    (3, 'Introduction to Algorithms',    'Thomas H. Cormen',  1200.00),
    (4, 'The C Programming Language',     'Brian W. Kernighan', 420.00),
    (5, 'Design Patterns',               'Erich Gamma',       750.00),
    (6, 'Refactoring',                   'Martin Fowler',     900.00),
    (7, 'Head First Java',               'Kathy Sierra',      390.00),
    (8, 'Database System Concepts',      'Abraham Silberschatz', 550.00);

-- 3) Filter: books priced above 500
SELECT * FROM books
WHERE price > 500;

-- 4) Sort all books by price (highest first)
SELECT * FROM books
ORDER BY price DESC;

-- 5) Count the total number of records
SELECT COUNT(*) AS total_books FROM books;

-- 6) Update a book's price using WHERE
UPDATE books
SET price = 500.00
WHERE title = 'Clean Code';

-- Verify the update
SELECT * FROM books
WHERE title = 'Clean Code';
