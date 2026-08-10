-- ====================================================================
-- DATABASE MANAGEMENT COMMANDS 
-- ====================================================================

-- 1. Create a Database
CREATE DATABASE IF NOT EXISTS database_name; 
-- This command creates a new database named 'database_name' if it does not already exist. 
-- It ensures that the database is created only once and avoids errors if it is already present.

-- 2. Drop / Delete a Database
DROP DATABASE IF EXISTS database_name; 
-- This command deletes the specified database if it exists. It is useful for removing a database 
-- and all its associated tables and data, but should be used with extreme caution as it is irreversible!

-- 3. List All Databases
SHOW DATABASES; 
-- This command is used to display a list of all databases available in the MySQL server. 
-- It helps users see which databases they can access and manage.

-- 4. Select a Database for Use
USE database_name; -- Note: Removed the keyword 'DATABASE' as standard MySQL syntax is just 'USE database_name;'
-- This command selects the specified database for use. All subsequent SQL commands 
-- (like creating tables or running queries) will be executed within the context of this active database.