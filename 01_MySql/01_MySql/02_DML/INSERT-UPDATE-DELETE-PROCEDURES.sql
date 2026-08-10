-- ====================================================================
-- 1. INSERT DATA INTO TABLE
-- ====================================================================

-- Note: When inserting multiple rows, the VALUES keyword is written only once, 
-- followed by comma-separated sets of parentheses.
INSERT INTO table_name (name, column1_name, column2_name) 
VALUES 
    ('value1_row1', 'value2_row1', 'value3_row1'),
    ('value1_row2', 'value2_row2', 'value3_row2'); 
-- This command inserts new rows into the specified table with the provided values for each column.


-- ====================================================================
-- 2. RETRIEVE DATA FROM TABLE
-- ====================================================================

SELECT * 
FROM table_name; 
-- This command retrieves all rows and columns from the specified table. 
-- It is used to view the data currently stored in the table.


-- ====================================================================
-- 3. UPDATE EXISTING DATA
-- ====================================================================

UPDATE table_name 
SET column1_name = 'new_value1', 
    column2_name = 'new_value2'
WHERE condition; 
-- This command updates existing rows in the specified table based on a given condition. 
-- Crucial Note: Always use a WHERE clause, otherwise all rows in the table will be updated!


-- ====================================================================
-- 4. DELETE SPECIFIC ROWS
-- ====================================================================

DELETE FROM table_name 
WHERE condition; 
-- This command deletes rows from the specified table that meet the given condition, 
-- allowing users to remove unwanted data while preserving the table structure.


-- ====================================================================
-- 5. STORED PROCEDURES (DEFINITION & EXECUTION)
-- ====================================================================

-- Changing the delimiter temporarily so the semicolon inside the procedure 
-- does not prematurely terminate the statement block
DELIMITER //

CREATE PROCEDURE GetEmployeeDetails (IN emp_id INT)
BEGIN
    -- This query is saved inside the database as a compiled block of logic
    SELECT employee_id, first_name, salary 
    FROM Employees 
    WHERE employee_id = emp_id;
END //

-- Resetting the delimiter back to the default semicolon
DELIMITER ;

-- Executing / Calling the stored procedure
CALL GetEmployeeDetails(101); 
-- This command executes a stored procedure in the database. 
-- Stored procedures are precompiled SQL statements that can perform complex operations 
-- and be reused multiple times.