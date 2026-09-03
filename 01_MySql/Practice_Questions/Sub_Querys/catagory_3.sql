-- Find employees who have the minimum salary in their respective departments ((department_id, salary) IN (...)).
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            MIN(salary)
        from employees
        GROUP BY department_id
    );
-- Find employees who have the maximum salary in their respective departments.
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            MAX(salary)
        from employees
        GROUP BY department_id
    );
-- Find employees whose department_id and salary match the department and salary of employee 102.
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            salary
        FROM employees
        WHERE emp_id = 102
    );
-- Find employees who share both the same department and same hire date as someone else in the table.
SELECT *
FROM employees
WHERE (department_id, hire_date) IN (
        SELECT department_id,
            hire_date
        FROM employees
        GROUP BY department_id,
            hire_date
        HAVING COUNT(*) > 1
    );
-- Find employees whose department_id and manager_id combination matches any department's leadership pattern.
SELECT *
FROM employees
WHERE (department_id, manager_id) IN (
        SELECT department_id,
            manager_id
        FROM employees
        GROUP BY department_id,
            manager_id
        HAVING COUNT(*) > 1
    );
-- Find employees whose emp_id and department_id exist in the project assignments as a valid pair.
SELECT *
FROM employees
WHERE (department_id, emp_id) IN (
        SELECT department_id,
            emp_id
        FROM projects
        WHERE emp_id IN (
                SELECT emp_id
                FROM project_assignments
            )
    );
-- Find employees whose job role and salary match the lowest paid tier per department.
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            MIN(salary)
        FROM employees
        GROUP BY department_id
    );
-- Find employees whose department and salary match the highest paid tier per department.
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            MAX(salary)
        FROM employees
        GROUP BY department_id
    );
-- Find employees whose department_id and salary are equal to any department's average metrics.
SELECT *
FROM employees
WHERE (department_id, salary) IN (
        SELECT department_id,
            ROUND(AVG(salary), 2)
        FROM employees
        GROUP BY department_id
    );
-- Find employees who match the department and minimum hire date of that department.
SELECT *
FROM employees
WHERE (department_id, hire_date) IN (
        SELECT department_id,
            MIN(hire_date)
        FROM employees
        GROUP BY department_id
    );