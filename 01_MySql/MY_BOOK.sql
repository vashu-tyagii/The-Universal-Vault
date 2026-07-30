-- SHOW DATABASES
SHOW DATABASES;

SELECT
	schema_name
FROM
	information_schema.schemata;

-- CREATE A DATABASE
CREATE DATABASE Local_DB;

-- TO USE DATABASE
USE Local_DB;

-- CHECK WHICH DB WE ARE USING
SELECT
	DATABASE ();

-- DELETE OR DROP DB
DROP DATABASE IF EXISTS demo;

-- CRUD OPERATIONS (CREATE, READ, UPDATE, DELETE)
-- CREATE TABLE
CREATE TABLE
	students (
		student_ID INT,
		name VARCHAR(100),
		age INT,
		grade INT
	);

-- CHECK EXISTING TABLES
SHOW TABLES LIKE 'students';

-- INSERTING DATA INTO TABLE
INSERT INTO
	students (student_ID, name, age, grade)
VALUES
	(101, 'Vashu Tyagi', 21, 10),
	(102, 'Shorya Sharma', 20, 10),
	(103, 'Prakash', 22, 9);

-- READ DATA
SELECT
	*
FROM
	students;

-- show complete data
SELECT
	name
FROM
	students;

-- show specific column data
-- UPDATE DATA / MODIFY DATA
UPDATE students
SET
	grade = 10
WHERE
	student_ID = 103;

-- DELETE DATA FROM TABLE
DELETE FROM students
WHERE
	student_ID = 103;

-- DELETE ENTIRE TABLE DATA
TRUNCATE TABLE students;

-- PRACTICE QUESTIONS
-- 1. WRITE QUERY TO CHANGE GRADE TO 9 --> 10
UPDATE students
SET
	grade = 10
WHERE
	student_ID = 103;

-- 2. ADD NEW STUDENT DATA
INSERT INTO
	students
VALUES
	(104, 'Mayank', 19, 10);

-- 3. WRITE A QUERY TO REMOVE A ROW FROM TABLE
DELETE FROM students
WHERE
	student_ID = 104;

-- 4. WRITE A QUERY TO RETRIEVE 1 ROW DATA FROM TABLE
SELECT
	*
FROM
	students
WHERE
	name = 'Vashu Tyagi';

-- 5. WRITE A QUERY TO PRINT/GET AGE OF SPECIFIC STUDENT
SELECT
	age
FROM
	students
WHERE
	name = 'Vashu Tyagi';

-- BASIC TO ADVANCED MYSQL QUERY GUIDE

-- 1) BASIC QUERIES

-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- Rename columns
SELECT first_name AS fname, last_name AS lname FROM employees;

-- Filter rows
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM employees
WHERE department_id = 2 AND salary > 50000;

-- Sort results
SELECT * FROM employees ORDER BY salary DESC;

-- Limit rows
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- Remove duplicates
SELECT DISTINCT department_id FROM employees;

-- 2) CONDITIONAL QUERIES

-- IN
SELECT * FROM employees
WHERE department_id IN (1, 2, 3);

-- BETWEEN
SELECT * FROM employees
WHERE salary BETWEEN 30000 AND 60000;

-- LIKE
SELECT * FROM employees
WHERE first_name LIKE 'J%';

-- NOT LIKE
SELECT * FROM employees
WHERE first_name NOT LIKE 'J%';

-- IS NULL / IS NOT NULL
SELECT * FROM employees
WHERE manager_id IS NULL;

-- 3) AGGREGATE FUNCTIONS

SELECT COUNT(*) AS total_employees FROM employees;
SELECT SUM(salary) AS total_salary FROM employees;
SELECT AVG(salary) AS avg_salary FROM employees;
SELECT MIN(salary) AS min_salary FROM employees;
SELECT MAX(salary) AS max_salary FROM employees;

-- Group by department
SELECT department_id, COUNT(*) AS total
FROM employees
GROUP BY department_id;

-- Filter grouped data
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;

-- 4) JOINS

-- INNER JOIN
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- LEFT JOIN
SELECT e.first_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- RIGHT JOIN
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;

-- SELF JOIN
SELECT e1.first_name AS employee, e2.first_name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;

-- 5) SUBQUERIES

-- Subquery in WHERE
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in SELECT
SELECT first_name,
       (SELECT department_name FROM departments WHERE id = employees.department_id) AS dept
FROM employees;

-- Subquery returning multiple rows
SELECT * FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York');

-- 6) SET OPERATIONS

-- UNION removes duplicates
SELECT id FROM employees
UNION
SELECT id FROM departments;

-- UNION ALL keeps duplicates
SELECT id FROM employees
UNION ALL
SELECT id FROM departments;

-- 7) DATA MANIPULATION LANGUAGE (DML)

-- Insert data
INSERT INTO employees (first_name, last_name, salary, department_id)
VALUES ('Amit', 'Sharma', 60000, 1);

-- Update data
UPDATE employees
SET salary = 65000
WHERE id = 1;

-- Delete data
DELETE FROM employees
WHERE id = 1;

-- Insert from another table
INSERT INTO employees_backup
SELECT * FROM employees;

-- 8) DATA DEFINITION LANGUAGE (DDL)

-- Create table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INT
);

-- Alter table
ALTER TABLE employees ADD COLUMN email VARCHAR(100);

-- Drop table
DROP TABLE employees;

-- Truncate table
TRUNCATE TABLE employees;

-- 9) CONSTRAINTS AND INDEXES

CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Create index
CREATE INDEX idx_salary ON employees(salary);

-- Drop index
DROP INDEX idx_salary ON employees;

-- 10) TRANSACTIONS

START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;

START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
ROLLBACK;

-- 11) ADVANCED QUERIES

-- Common Table Expressions (CTE)
WITH high_salary AS (
    SELECT id, first_name, salary
    FROM employees
    WHERE salary > 70000
)
SELECT * FROM high_salary;

-- Window functions
SELECT
    first_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank_salary
FROM employees;

SELECT
    department_id,
    first_name,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) AS dept_avg
FROM employees;

SELECT
    first_name,
    salary,
    SUM(salary) OVER (ORDER BY salary) AS running_total
FROM employees;

SELECT
    id,
    first_name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM employees;

-- 12) VIEWS

CREATE VIEW high_paid_employees AS
SELECT id, first_name, salary
FROM employees
WHERE salary > 60000;

SELECT * FROM high_paid_employees;

-- 13) STORED PROCEDURES AND FUNCTIONS

DELIMITER $$
CREATE PROCEDURE get_employee_count()
BEGIN
    SELECT COUNT(*) FROM employees;
END$$
DELIMITER ;

CALL get_employee_count();

DELIMITER $$
CREATE FUNCTION get_total_salary()
RETURNS DECIMAL(10,2)
BEGIN
    RETURN (SELECT SUM(salary) FROM employees);
END$$
DELIMITER ;

-- FULL ADVANCED EXAMPLE
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department_id
)
SELECT
    e.first_name,
    e.salary,
    d.department_name,
    da.avg_sal,
    RANK() OVER (ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.id
JOIN dept_avg da ON e.department_id = da.department_id
WHERE e.salary > da.avg_sal
ORDER BY e.salary DESC;

-- BEST PRACTICE TIPS
-- Use SELECT with only needed columns.
-- Always filter with WHERE instead of fetching everything.
-- Use indexes on frequently searched columns.
-- Avoid SELECT * in large tables.
-- Use JOIN carefully and test with LIMIT.
