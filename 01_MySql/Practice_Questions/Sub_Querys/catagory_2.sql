-- Find all employees who work in departments located in 'Bangalore', 'Hyderabad', or 'Mumbai'.
SELECT *
FROM employees
WHERE department_id IN (
                SELECT department_id
                FROM departments
                WHERE location IN(
                                'Bangalore',
                                'Hyderabad',
                                'Mumbai'
                        )
        );
-- Find employees whose salaries match the salary of any manager in the company (manager_id IS NULL).
SELECT *
FROM employees
WHERE salary > (
                SELECT MAX(salary)
                FROM employees
                WHERE manager_id IS NULL
        );
-- Find employees who do not work in the 'Engineering' or 'Finance' departments.
SELECT *
FROM employees
WHERE department_id NOT IN(
                SELECT department_id
                FROM departments
                WHERE dep_name IN(
                                'Engineering',
                                'Finance'
                        )
        );
-- Find employees whose salary is greater than all salaries of employees in the 'Human Resources' department.
SELECT *
FROM employees
where salary > ALL(
                SELECT salary
                FROM departments
                where dep_name = 'Human Resources'
        );
-- Find employees who work in departments that have more than 5 employees.
SELECT *
FROM employees
WHERE department_id IN (
                SELECT department_id
                FROM employees
                GROUP BY department_id
                HAVING COUNT(*) > 5
        );
-- Find employees assigned to projects with a budget greater than 400,000.
SELECT *
FROM employees
WHERE emp_id IN (
                SELECT emp_id
                FROM project_assignments
                WHERE project_id IN (
                                SELECT project_id
                                FROM projects
                                WHERE budget > 400000
                        )
        );
-- Find employees whose job roles match any job role in the 'Data Science' department.
SELECT *
FROM employees
WHERE job_role IN (
                SELECT job_role
                FROM employees
                WHERE department_id = (
                                SELECT department_id
                                FROM departments
                                WHERE dep_name = 'Data Science'
                        )
        );
-- Find employees who are not assigned to any project in the project_assignments table (NOT IN).
SELECT *
FROM employees
WHERE emp_id NOT IN (
                SELECT emp_id
                FROM project_assignments
        );
-- Find employees working in departments where the location starts with the letter 'B'.
SELECT *
FROM employees
WHERE department_id = (
                SELECT department_id
                FROM departments
                WHERE location LIKE 'B%'
        );
SELECT *
FROM departments;
-- Find employees whose salaries are in the list of top 5 highest salaries in the company.
SELECT *
FROM employees
WHERE salary IN (
                SELECT salary
                FROM (
                                SELECT salary
                                FROM employees
                                ORDER BY salary DESC
                                LIMIT 5
                        ) AS temp_top5
        );