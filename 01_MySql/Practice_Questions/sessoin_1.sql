-- 1. Create and Use Database
CREATE DATABASE IF NOT EXISTS company_db;

USE company_db;

-- 2. Create DEPARTMENT Table First (Kyunki yeh Parent table hai)
CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY COMMENT "Unique identifier for the department",
    department_name VARCHAR(50) COMMENT "Name of the department",
    location VARCHAR(50) COMMENT "Location of the department"
);

-- 3. Create EMPLOYEES Table (Child Table with Table-Level Foreign Key)
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY COMMENT "Employee ID",
    first_name VARCHAR(50) COMMENT "Employee first name",
    last_name VARCHAR(50) COMMENT "Employee last name",
    email VARCHAR(50) UNIQUE COMMENT "Unique employee email address",
    hire_date DATE DEFAULT (CURRENT_DATE) COMMENT "Employee hiring date",
    salary DECIMAL(10, 2) COMMENT "Employee salary",
    department_id INT COMMENT "Department ID",

    -- Table-level Foreign Key definition
    CONSTRAINT fk_employees_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 4. Modify Employee Table (Salary > 0 Check Constraint)
ALTER TABLE employees
ADD CONSTRAINT chk_salary CHECK (salary > 0);

-- 5. Modify Table Employees (Set NOT NULL on names)
ALTER TABLE employees
MODIFY first_name VARCHAR(50) NOT NULL,
    MODIFY last_name VARCHAR(50) NOT NULL;

-- 6. Add and Test Alter Operations (Add, Rename, Drop Column)
ALTER TABLE employees ADD COLUMN phone_no VARCHAR(15) NOT NULL;
ALTER TABLE employees RENAME COLUMN phone_no TO contact_number;
ALTER TABLE employees DROP COLUMN contact_number;

-- 7. Insert Data Into Departments (Parent Table First)
INSERT INTO departments (department_id, department_name, location)
    VALUES (1, 'IT', 'DELHI'),
        (2, 'IT', 'GURUGRAM');

-- 8. Insert Data Into Employees (Child Table)
INSERT INTO employees (
        emp_id,first_name,last_name,email,salary,department_id
    )
VALUES (
        101,'Vashu','Tyagi','vashu.tyagi.connect@gmail.com',30000,1
    ),
    (
        102,'Vashu','Tyagi','vashu.tyagi.me@gmail.com',40000,2
    );

-- 9. View Data
SELECT * FROM employees;
SELECT * FROM departments;

-- 10. Delete Specific Row
DELETE FROM employees WHERE emp_id = 101;

-- CREATING DELIMITER FOR ENTER DATA INTO EMPLOYEES OR DEPARTMENT TABLES COMMENT
DELIMITER // CREATE PROCEDURE data_in_employees(
    IN p_emp_id INT,
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(50),
    IN p_hire_date DATE,
    IN p_salary DECIMAL(10, 2),
    IN p_department_id INT
) COMMENT 'Insert a new employee' BEGIN
INSERT INTO employees (
        emp_id,first_name,last_name,email,hire_date,salary,department_id
    )
VALUES (
        p_emp_id,p_first_name,p_last_name,p_email,
        COALESCE(p_hire_date, CURRENT_DATE),
        p_salary,p_department_id
    );
END //

-- CREATE VIEW TO SHOW BOTH TABLES EMPLOYEES AND DEPARTMENT
CREATE VIEW employee_department_view AS
SELECT 
    e.emp_id,
    e.first_name,
    e.last_name,
    e.email,
    e.salary,
    d.dep_name,
    d.location
FROM employees e, departments d
WHERE e.department_id = d.department_id;

-- CALLING VIEW
SELECT * FROM employee_department_view ;

