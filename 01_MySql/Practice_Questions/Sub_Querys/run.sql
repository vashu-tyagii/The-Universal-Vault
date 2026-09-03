-- Find employees whose salary is greater than the average salary of the entire company
SELECT *
FROM employees
WHERE salary < (
        SELECT AVG(salary)
        FROM employees
    );