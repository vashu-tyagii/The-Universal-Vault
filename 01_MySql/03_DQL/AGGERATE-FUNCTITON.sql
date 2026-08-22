-- Aggregate function examples

SELECT COUNT(*) AS total_rows
FROM employees;

SELECT
	COUNT(*) AS employee_count,
	SUM(salary) AS total_salary,
	AVG(salary) AS average_salary,
	MIN(salary) AS lowest_salary,
	MAX(salary) AS highest_salary
FROM employees;

