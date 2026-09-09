SELECT 
ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
    first_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rnk,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk
FROM employees;

SELECT 
    emp_id,
    first_name,
    department_id,
    salary,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_salary_rank
FROM employees;

SELECT 
    emp_id,
    salary,
    LAG(salary, 1) OVER (ORDER BY emp_id) AS previous_salary
FROM employees;

SELECT 
    emp_id,
    salary,
    LEAD(salary, 1) OVER (ORDER BY emp_id) AS next_salary
FROM employees;

SELECT 
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;