/*
	GROUP BY and HAVING
	Examples use the commonly available `employees` table:
	employees(id, first_name, last_name, department, job_title,
				 salary, city, gender, hire_date)
*/

-- GROUP BY combines rows with the same value.
SELECT department
FROM employees
GROUP BY department;

-- Aggregate functions with GROUP BY
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT department,
		 COUNT(*) AS employee_count,
		 SUM(salary) AS total_salary,
		 AVG(salary) AS average_salary,
		 MIN(salary) AS lowest_salary,
		 MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

-- Group by more than one column
SELECT department, city, COUNT(*) AS employee_count
FROM employees
GROUP BY department, city;

-- Group by an expression
SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS employees_hired
FROM employees
GROUP BY YEAR(hire_date)
ORDER BY hire_year;

-- GROUP BY with WHERE: WHERE filters rows before grouping
SELECT department, AVG(salary) AS average_salary
FROM employees
WHERE salary >= 30000
GROUP BY department;

-- HAVING filters groups after GROUP BY
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) >= 5;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- HAVING can contain multiple conditions
SELECT department,
		 COUNT(*) AS employee_count,
		 SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING COUNT(*) >= 3
	AND SUM(salary) > 200000;

-- WHERE and HAVING together
SELECT department,
		 COUNT(*) AS employee_count,
		 AVG(salary) AS average_salary
FROM employees
WHERE city = 'London'
GROUP BY department
HAVING AVG(salary) >= 50000;

-- GROUP BY with ORDER BY and LIMIT
SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department
HAVING MAX(salary) > 80000
ORDER BY highest_salary DESC
LIMIT 5;

-- DISTINCT alternative for unique values (no aggregation)
SELECT DISTINCT department
FROM employees;

-- GROUP BY all non-aggregated selected columns
SELECT department, job_title, COUNT(*) AS employee_count
FROM employees
GROUP BY department, job_title
ORDER BY department, employee_count DESC;

/* Query order:
	FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

	WHERE cannot normally use aggregate results:
	-- WHERE COUNT(*) > 5       -- invalid
	HAVING COUNT(*) > 5          -- correct
*/
