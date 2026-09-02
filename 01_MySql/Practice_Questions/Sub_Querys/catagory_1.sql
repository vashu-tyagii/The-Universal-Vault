-- Find the employee(s) who earn the highest salary in the company.
SELECT *
FROM employees
WHERE salary =(
        SELECT MAX(salary)
        FROM employees
    );
-- Find all employees who earn less than the average salary of the entire company.
SELECT CONCAT(first_name, ' ', last_name) AS Emp_Name,
    salary
FROM employees
WHERE salary < (
        SELECT AVG(salary)
        FROM employees
    );
-- Find employees who were hired earlier than the employee with emp_id = 105.
SELECT *
FROM employees
where hire_date > (
        SELECT hire_date
        FROM employees
        where emp_id = 105
    );
-- Find the employee(s) who have the exact minimum salary in the company.
SELECT *
FROM employees
WHERE salary =(
        SELECT MIN(salary)
        FROM employees
    );
-- Find employees whose salary is greater than employee 102's salary.
SELECT *
FROM employees
where salary > (
        SELECT salary
        FROM employees
        where emp_id = 102
    );
-- Find employees working in the same department as employee 115.
SELECT *
FROM employees
WHERE department_id = (
        SELECT department_id
        FROM employees
        WHERE emp_id = 115
    );
-- Find employees whose salary is equal to the maximum salary of the company.
SELECT *
FROM employees
WHERE salary =(
        SELECT MAX(salary)
        FROM employees
    );
-- Find employees who earn more than the employee named 'Vikram' (first_name = 'Vikram').
SELECT *
FROM employees
WHERE salary < (
        SELECT salary
        FROM employees
        WHERE first_name = 'Vikram'
    );
-- Find employees hired on the exact same date as the earliest hire date in the company.
SELECT *
FROM employees
WHERE hire_date = (
        SELECT MAX(hire_date)
        FROM employees
    );
-- Find employees whose salary is less than the maximum salary in the company.
SELECT *
FROM employees
WHERE salary <(
        SELECT MAX(salary)
        FROM employees
    );