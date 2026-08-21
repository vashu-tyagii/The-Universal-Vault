-- 1. Write a query to fetch all columns for all employees.
SELECT *
FROM employees;
-- 2. Fetch the unique product from the orders table.
SELECT DISTINCT products
FROM orders;
-- 3. Fetch all details of employees who belong to the 'Sales' department.
SELECT *
FROM employees
WHERE department = 'Sales';
-- 4. Fetch the employee names and their salaries with column aliases "Name" and "Income"
SELECT CONCAT(first_name, ' ', last_name) AS Name,
    salary AS Income
FROM employees;
-- 5. Show all products buy price above 50 Dollar.
SELECT *
FROM orders
WHERE price >= 50;
-- 6. Fetch the top 2 highest paid employees in our company.
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 2;
-- 7. Get employees who are either in Sales or have a salary above 30,000.
SELECT *
FROM employees
WHERE department = 'Sales'
    OR salary >= 30000;
-- 8. Fetch products with a price between 20 and 100.
SELECT *
FROM products
WHERE price BETWEEN 20 AND 100;
-- 9. Retrieve orders where the product is either 'Laptop' or 'Tablet'
SELECT *
FROM products
WHERE product_name IN ('Laptop', 'Tablet');
-- 10. Find employee names starting with 'J'
SELECT *
FROM employees
WHERE first_name LIKE 'J%';
-- 11. Case insensitive search for employee names containing 'son'
SELECT *
FROM employees
WHERE first_name LIKE '%son%';
-- 12. Display employee names along with their salary category as 'High' if above 70,000, else 'Low'
SELECT *,
    CASE
        WHEN salary >= 70000 THEN 'HIGH'
        ELSE 'LOW'
    END AS RANK_FOR_SALARY
FROM employees;
-- Additional queries
-- Show the delivery date, but if it is NULL, display 'Pending'
SELECT order_id,
    COALESCE(delivery_date, 'Pending') AS delivery_status
FROM orders;
-- Compare two columns and return NULL if they are the same (NULLIF)
SELECT employee_id,
    salary,
    bonus,
    NULLIF(salary, bonus) AS adjusted_salary
FROM employees;
-- Display employee names and their salary incremented by 10% as "New Salary"
SELECT CONCAT(first_name, ' ', last_name) AS Name,
    salary * 1.10 AS "New Salary"
FROM employees;
-- Get the employees who are either in 'Sales' or 'Marketing' department and earn more than 30,000.
SELECT *
FROM employees
WHERE department IN ('Marketing', 'Sales')
    AND salary > 30000;
-- Show the product name and its availability status as 'In Stock' if the quantity is more than 0, else 'Out of Stock'
SELECT product_name,
    CASE
        WHEN stock > 0 THEN 'In Stock'
        ELSE 'Out of Stock'
    END AS availability_status
FROM products;
-- Display customer names and delivery dates, but if the delivery date is NULL, show 'Not Delivered'
SELECT customer_name,
    IFNULL(delivery_date, 'Not Delivered') AS delivery_status
FROM orders;
-- Retrieve all products whose names contain the letter 'a' (case insensitive) and are priced between 50 and 200, ordered by price in ascending order.
SELECT *
FROM products
WHERE product_name LIKE '%a%'
    AND price BETWEEN 50 AND 200
ORDER BY price ASC;
-- Count the number of different products sold.
SELECT COUNT(DISTINCT product_name) AS unique_products_count
FROM order_items;
-- Count how many employees have salaries above 70,000.
SELECT COUNT(*) AS high_earners_count
FROM employees
WHERE salary > 70000;