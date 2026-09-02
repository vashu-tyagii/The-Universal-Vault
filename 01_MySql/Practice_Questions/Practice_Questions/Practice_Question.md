# SQL Practice Questions — Generic, Basic to Advance

No specific dataset required — create your own tables as instructed in each 
section. Work through this in order; each section builds on tables created 
in earlier ones.

**Rule: Attempt every question yourself first. Run it, see the result, THEN 
move to the next one.**

---

## Section 1 — Database & Table Creation, Data Types, Constraints

1. Create a database called `company_db`.
2. Inside it, create a table `employees` with: emp_id (INT, Primary Key), 
   first_name (VARCHAR 50), last_name (VARCHAR 50), email (VARCHAR 100, UNIQUE), 
   hire_date (DATE), salary (DECIMAL 10,2), department_id (INT).
3. Create a second table `departments` with: department_id (INT, Primary Key), 
   department_name (VARCHAR 50), location (VARCHAR 50).
4. Add a FOREIGN KEY constraint linking employees.department_id to departments.department_id.
5. Add a CHECK constraint ensuring salary is always greater than 0.
6. Add a NOT NULL constraint on first_name and last_name (if not already set).
7. Alter the employees table to add a new column `phone` (VARCHAR 15).
8. Rename the `phone` column to `contact_number`.
9. Drop the `contact_number` column.
10. Truncate a test table (create a throwaway table first, insert a few rows, then truncate it — observe that the structure remains but data is gone).

---

## Section 2 — Inserting & Managing Data (DML)

1. Insert 5 departments into the `departments` table (e.g., Sales, HR, IT, Finance, Marketing).
2. Insert 15 employees into the `employees` table, spread across the 5 departments, 
   with varying salaries and hire dates.
3. Update the salary of one employee by giving them a 10% raise.
4. Update all employees in one department to a new department_id (simulate a department merge).
5. Delete one employee record by emp_id.
6. Delete all employees hired before a certain date (pick a cutoff date).
7. Insert a new employee using values selected from another table (INSERT INTO ... SELECT), 
   if you have a second similar table to pull from.

---

## Section 3 — SELECT Fundamentals

1. Select all columns from employees.
2. Select only first_name, last_name, and salary.
3. Select distinct department_id values from employees.
4. Find all employees with salary greater than 50000.
5. Find all employees hired after a specific date.
6. Sort employees by salary in descending order.
7. Show only the top 5 highest-paid employees.
8. Find employees whose email contains "gmail".
9. Find employees NOT in department_id 2 or 3.
10. Using CASE, label employees as "Senior" (salary > 70000) or "Junior" (salary <= 70000).

---

## Section 4 — JOINs

1. INNER JOIN employees and departments to show each employee's department name.
2. LEFT JOIN to show all employees, including any whose department_id doesn't match a department (if any).
3. RIGHT JOIN to show all departments, including any with no employees.
4. FULL OUTER JOIN to show all employees and all departments together (MySQL doesn't support FULL JOIN directly — simulate with UNION of LEFT and RIGHT JOIN).
5. CROSS JOIN employees and departments (observe the row count — rows_employees × rows_departments).
6. SELF JOIN: find pairs of employees who work in the same department.

---

## Section 5 — Aggregation, GROUP BY, HAVING

1. Find the total salary paid per department.
2. Find the average salary per department.
3. Find the number of employees per department.
4. Find the highest and lowest salary overall.
5. Find departments where the average salary is above 60000 (use HAVING).
6. Find departments with more than 3 employees (use HAVING).
7. Find the department with the highest total salary expenditure.

---

## Section 6 — Subqueries

1. Find employees who earn more than the average salary (subquery in WHERE).
2. Find the employee with the highest salary using a subquery instead of ORDER BY + LIMIT.
3. Find departments that have no employees (subquery with NOT IN or NOT EXISTS).
4. Find the second-highest salary in the company (classic interview question — try 2-3 different methods).
5. Find employees who earn more than the average salary of their own department (correlated subquery).

---

## Section 7 — String, Date & Time Functions

1. Convert all first_name values to uppercase.
2. Concatenate first_name and last_name into a "full_name" column.
3. Find the length of each email address.
4. Extract the year from hire_date for each employee.
5. Calculate how many days each employee has been with the company (DATEDIFF from hire_date to today).
6. Find employees hired in a specific month, regardless of year.

---

## Section 8 — Window Functions

1. Rank employees within each department by salary (RANK()).
2. Assign row numbers to employees ordered by hire_date.
3. Find the top 2 highest-paid employees per department using ROW_NUMBER() + PARTITION BY.
4. Show each employee's salary alongside the department's average salary (window AVG() OVER PARTITION BY).
5. Use LAG() to show the previous employee's salary when employees are ordered by hire_date.
6. Calculate a running total of salaries ordered by hire_date.

---

## Section 9 — Views, Temp Tables, Indexes

1. Create a view `high_earners` showing employees with salary > 70000.
2. Query the view with an additional WHERE filter.
3. Create a temporary table holding only employees hired in the last year.
4. Create an index on the department_id column in employees, and explain why this could speed up JOIN queries.

---

## Section 10 — TCL & DCL

1. Start a transaction, update an employee's salary, then ROLLBACK — verify it reverted.
2. Start a transaction, update an employee's salary, then COMMIT — verify it stuck.
3. Use SAVEPOINT within a multi-statement transaction, roll back to the savepoint only.
4. (Conceptual) Write what GRANT SELECT, INSERT ON employees TO 'analyst_user' would do.
5. (Conceptual) Write what REVOKE DELETE ON employees FROM 'analyst_user' would do.

---

## Section 11 — Stored Procedures & Functions

1. Write a stored procedure `GetEmployeesByDept` that takes a department_id and returns all employees in it.
2. Write a stored procedure that gives every employee in a given department a raise by a percentage passed as a parameter.
3. Write a simple function that returns the number of years an employee has worked, given their hire_date.

---

## Section 12 — Final Mixed Practice (Combine Everything)

1. Full pipeline: JOIN employees + departments, GROUP BY department, HAVING avg salary > X, ORDER BY total salary DESC.
2. Find the 3rd highest salary using window functions.
3. Find duplicate email entries (if any exist) using GROUP BY + HAVING COUNT > 1.
4. Rank departments by total salary expenditure using DENSE_RANK().
5. Combine a subquery + JOIN + window function in a single complex query — attempt your own scenario.