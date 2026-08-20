-- SHOW DEPARTMENT, EMPLOYEES TABLES
SELECT * FROM departments;
SELECT * FROM employees;

-- INSERTING DEP INTO DEPARTMENTS TABLES
INSERT INTO departments ()
VALUES (3, 'Sales',' NOIDA'),
    (4,'Finance','HYDERABAD'),
    (5,'Marketing','BANGALORE');

--
INSERT INTO employees (emp_id, first_name, last_name, email, salary, department_id)
VALUES 
    (101, 'Vashu', 'Tyagi', 'vashu.tyagi.connect@gmail.com', 30000, 1),
    (102, 'Vansh', 'Tyagi', 'vansh.tyagi.connect@gmail.com', 40000, 2),
    (103, 'Vikas', 'Tyagi', 'vikas.tyagi.connect@gmail.com', 30000, 3),
    (104, 'Aarav', 'Sharma', 'aarav.sharma@gmail.com', 35000, 4),
    (105, 'Ananya', 'Verma', 'ananya.verma@gmail.com', 45000, 5);

-- GIVE ONE EMPLOYEE A 10% RAISE
UPDATE employees SET salary = salary * 1.10
WHERE emp_id = 101;

-- MERGE DEPARTMENT 5 INTO DEPARTMENT 3
UPDATE employees SET department_id = 3
WHERE department_id = 5;

-- DELETE ONE EMPLOYEE
DELETE FROM employees
WHERE emp_id = 105;

-- DELETE EMPLOYEES HIRED BEFORE THE CUTOFF DATE
DELETE FROM employees
WHERE hire_date < '2023-01-01';

