-- UNION, UNION ALL, EXCEPT, INTERSECT examples
-- MySQL 8+ supports UNION and UNION ALL natively.

CREATE TABLE employees_2023 (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE employees_2024 (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO employees_2023 (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');

INSERT INTO employees_2024 (id, name) VALUES
(2, 'Bob'),
(3, 'Charlie'),
(5, 'Eve'),
(6, 'Frank');

-- UNION: removes duplicate rows
SELECT name
FROM employees_2023
UNION
SELECT name
FROM employees_2024;

-- UNION ALL: keeps duplicate rows
SELECT name
FROM employees_2023
UNION ALL
SELECT name
FROM employees_2024;

