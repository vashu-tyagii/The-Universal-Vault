-- Example: Create table
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    created_at DATETIME
);

-- Simple index on a single column
CREATE INDEX idx_users_email ON users(email);

-- Composite index on multiple columns
CREATE INDEX idx_users_city_created_at ON users(city, created_at);

-- Unique index (prevents duplicate values)
CREATE UNIQUE INDEX uq_users_email ON users(email);

-- Example query using the index
SELECT *
FROM users
WHERE email = 'demo@example.com';

SELECT *
FROM users
WHERE city = 'Delhi'
ORDER BY created_at DESC;
