-- ====================================================================
-- 1. CREATE TABLE
-- ====================================================================

CREATE TABLE IF NOT EXISTS table_name (
    -- Fixed: In standard SQL/MySQL, VARCHAR is used instead of STRING(100) inside table definitions.
    name VARCHAR(100) NOT NULL COMMENT 'This is a comment for the name column', 
    column1_name VARCHAR(50) NOT NULL,
    column2_name INT,
    
    -- Table-level Primary Key definition
    CONSTRAINT pk_table_name PRIMARY KEY (name)
); 
-- This command creates a new table named 'table_name' with specified columns and their data types. 
-- It also defines the primary key for the table. The 'IF NOT EXISTS' clause ensures that the table 
-- is created only if it does not already exist, preventing errors if the table already exists.


-- ====================================================================
-- 2. INSPECTING TABLES AND COLUMNS
-- ====================================================================

-- Note: Standard MySQL uses 'SHOW TABLES;' or 'SHOW FULL TABLES;'
SHOW FULL TABLES; 
-- This command displays a list of all tables in the currently selected database, along with additional information 
-- such as the table type. It helps users see which tables are available for use. 

SHOW FULL COLUMNS FROM table_name; -- (Updated 'Users' to match your table_name)
-- This command displays detailed information about the columns in the specified table. It provides information 
-- such as column names, data types, default values, and any constraints applied.


-- ====================================================================
-- 3. CREATE AND QUERY A VIEW
-- ====================================================================

-- Note: Standard SQL syntax for CREATE VIEW does not use 'IF NOT EXISTS'. 
-- To safely handle existing views, use 'CREATE OR REPLACE VIEW'.
CREATE OR REPLACE VIEW view_name AS
    SELECT column1_name, column2_name 
    FROM table_name 
    WHERE column2_name > 10; 
-- This command creates or replaces a view named 'view_name' based on a SELECT query from the specified table. 
-- Views are virtual tables that can simplify complex queries and provide a layer of abstraction.

-- Note: In MySQL, to see views, you typically use 'SHOW TABLES;' (since views are listed alongside tables) 
-- or query the information schema, as 'SHOW VIEWS;' is not a standard native command.
SHOW FULL TABLES WHERE Table_type = 'VIEW'; 
-- This command helps filter and display a list of all views in the currently selected database.

SELECT * FROM view_name; 
-- This command retrieves all records from the specified view, allowing users to query and analyze 
-- the data presented by it.


-- ====================================================================
-- 4. ALTER TABLE OPERATIONS
-- ====================================================================

ALTER TABLE table_name
    ADD new_column_name VARCHAR(100) NOT NULL; 
-- This command adds a new column to an existing table.

ALTER TABLE table_name
    DROP COLUMN new_column_name; 
-- This command removes a specified column from an existing table.

ALTER TABLE table_name
    MODIFY COLUMN column2_name BIGINT; 
-- This command changes the data type or constraints of an existing column in a table.

ALTER TABLE table_name
    RENAME COLUMN column1_name TO updated_column_name; 
-- This command renames an existing column in a table to better reflect its purpose.


-- ====================================================================
-- 5. REMOVING DATA OR TABLES (DROP, TRUNCATE, DELETE)
-- ====================================================================

DROP TABLE IF EXISTS table_name; 
-- This command deletes the specified table and all its associated data completely. Use with caution!

TRUNCATE TABLE table_name; 
-- This command removes all records from the specified table while keeping the table structure intact. 
-- It is much faster than DELETE and resets auto-increment counters.

DELETE FROM table_name WHERE column2_name = 0; 
-- This command deletes specific records from the specified table based on a given condition, 
-- allowing you to keep the rest of the table's contents safe.