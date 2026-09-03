-- Find employees whose salary is greater than the average salary of their own department.
SELECT e.*
FROM employees e
WHERE salary > (
        SELECT Avg(e2.salary)
        FROM employees e2
        WHERE e.department_id = e2.department_id
    );
-- Find employees whose salary is the maximum in their respective department.
SELECT e.*
FROM employees e
WHERE salary = (
        SELECT MAX(e2.salary)
        FROM employees e2
        WHERE e.department_id = e2.department_id
    );
-- Find employees who earn less than the average salary of their department.
SELECT e.*
FROM employees e
WHERE salary < (
        SELECT Avg(e2.salary)
        FROM employees e2
        WHERE e.department_id = e2.department_id
    );
-- Find employees who were hired before their department's average hire date.
SELECT e.*
FROM employees e
WHERE hire_date < (
        SELECT Avg(e2.hire_date)
        FROM employees e2
        WHERE e.department_id = e2.department_id
    )
ORDER BY hire_date DESC;
-- Find employees who earn more than any other employee in a different department.
SELECT e1.*
FROM employees e1
WHERE e1.salary > ALL (
        SELECT e2.salary
        FROM employees e2
        WHERE e1.department_id != e2.department_id
    );
-- Find managers (manager_id IS NULL) who earn more than the average salary of the team members reporting to them.
SELECT e1.*
FROM employees e1
WHERE e1.salary > (
        SELECT AVG(e2.salary)
        FROM employees e2
        WHERE e1.emp_id = e2.manager_id
    );

-- Find employees whose salary is equal to the maximum salary in their respective department.
SELECT e1.*
FROM employees e1
WHERE salary = (
        SELECT MAX(e2.salary)
        FROM employees e2
        WHERE e1.department_id = e2.department_id
    );
-- Find employees who are the only ones earning above 90,000 in their department.
SELECT e1.*
FROM employees e1
WHERE e1.salary > 90000
    AND (
        SELECT COUNT(*)
        FROM employees e2
        WHERE e2.department_id = e1.department_id
            AND e2.salary > 90000
    ) = 1;
-- Find employees whose employee ID is greater than the average employee ID of their department.
SELECT e1.*
FROM employees e1
WHERE emp_id > (
        SELECT AVG(e2.emp_id)
        FROM employees e2
        WHERE e1.department_id = e2.department_id
    );