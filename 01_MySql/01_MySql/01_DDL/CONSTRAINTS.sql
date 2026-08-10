CREATE TABLE IF NOT EXISTS all_constraints_master (
    -- ====================================================================
    -- 1. PRIMARY KEY CONSTRAINT
    -- ====================================================================
    -- Uniquely identifies each record in a table. 
    -- It cannot contain NULL values, and must contain unique values.
    employee_id INT NOT NULL COMMENT 'Unique identifier for every employee; acts as the primary key.',

    -- ====================================================================
    -- 2. NOT NULL CONSTRAINT
    -- ====================================================================
    -- Ensures that a column cannot store a NULL (empty) value.
    first_name VARCHAR(50) NOT NULL COMMENT 'First name of the employee; cannot be left blank/NULL.',

    -- ====================================================================
    -- 3. UNIQUE CONSTRAINT
    -- ====================================================================
    -- Ensures that all values in a column are completely distinct from one another.
    email VARCHAR(100) UNIQUE COMMENT 'Email address must be unique; no two employees can share the same email.',

    -- ====================================================================
    -- 4. CHECK CONSTRAINT
    -- ====================================================================
    -- Ensures that all values in a column satisfy a specific logical condition.
    age INT CHECK (age >= 18) COMMENT 'Age restriction constraint; employee must be at least 18 years old.',

    -- ====================================================================
    -- 5. DEFAULT CONSTRAINT
    -- ====================================================================
    -- Provides a default fallback value for a column if no explicit value is provided during insertion.
    joining_date DATE DEFAULT (CURRENT_DATE) COMMENT 'Automatically assigns the current system date if no joining date is provided.',

    -- ====================================================================
    -- 6. FOREIGN KEY CONSTRAINT (Child Table Reference)
    -- ====================================================================
    -- Used to link two tables together. It acts as a cross-reference between tables 
    -- by referencing the Primary Key of another parent table.
    dept_id INT COMMENT 'Department ID referencing the parent Departments table for relational integrity.',

    -- ====================================================================
    -- TABLE-LEVEL CONSTRAINT DECLARATIONS
    -- ====================================================================
    
    -- Declaring the Primary Key at the table level
    CONSTRAINT pk_employee PRIMARY KEY (employee_id),

    -- Declaring the Foreign Key at the table level with ON DELETE/UPDATE rules
    CONSTRAINT fk_department_ref FOREIGN KEY (dept_id) 
        REFERENCES Departments(dept_id) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE

); -- This comprehensive script creates a blueprint table named 'all_constraints_master' demonstrating all core SQL constraints (Primary Key, Foreign Key, Unique, Check, Not Null, and Default) with inline technical documentation.

--==================================================================================
-- Example of Foreign Key Constraint with Parent-Child Relationship
--==================================================================================

-- Step 1: Create Parent Table (Students)
CREATE TABLE Students (
    stu_id INT PRIMARY KEY,
    stu_name VARCHAR(100) NOT NULL
);

-- Step 2: Create Child Table (Enrollments) with Foreign Key
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    stu_id INT,
    -- Yeh rahi Foreign Key jo Table 1 (Students) ke stu_id se judi hai
    CONSTRAINT fk_student FOREIGN KEY (stu_id) 
        REFERENCES Students(stu_id)
        ON DELETE CASCADE -- This means if a student record is deleted from the Students table, all corresponding enrollment records in the Enrollments table will also be automatically deleted.
        ON UPDATE CASCADE -- This means if the stu_id in the Students table is updated, the corresponding stu_id in the Enrollments table will also be automatically updated to maintain referential integrity.
);