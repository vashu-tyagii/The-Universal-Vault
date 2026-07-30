# SQL Complete Mastery Blueprint - Vashu Tyagi

This repository contains a complete, structured master guide covering everything from basic database structure to advanced analytical queries and security control, for Data Analysts and Data Engineers.

---

## Table of Contents

1. [Introduction & Setup](#0-introduction--setup)
2. [DDL (Data Definition Language)](#1-ddl-data-definition-language)
3. [DML (Data Manipulation Language)](#2-dml-data-manipulation-language)
4. [DQL (Data Query Language)](#3-dql-data-query-language)
5. [TCL (Transaction Control Language)](#4-tcl-transaction-control-language)
6. [DCL (Data Control Language)](#5-dcl-data-control-language)
7. [Advanced Analytics & Architecture](#6-advanced-analytics--architecture)

---

## 0. Introduction & Setup

*Focus: Foundational understanding before writing any SQL.*

* Introduction to Databases
* Overview of Databases (relational structure, tables, rows, columns)
* Applications & Jobs (where SQL is used, career relevance)
* Software Installation (MySQL Server + MySQL Workbench)
* Database Setup (creating first connection, first database)
* Tables Creation & First Query

---

## 1. DDL (Data Definition Language)

*Focus: Managing the structure, schema, and containers of the database.*

* **Database Management**
  * `CREATE DATABASE` - Initializing a new database container.
  * `DROP DATABASE` - Permanently deleting a database and its contents.
* **Table Management**
  * `CREATE TABLE` - Designing tables with structural columns.
  * `ALTER TABLE` - Modifying existing schemas (`ADD`, `MODIFY`, `DROP`, `RENAME COLUMN`).
  * `DROP TABLE` - Completely removing a table structure and data.
  * `TRUNCATE TABLE` - Clearing all rows rapidly while keeping the structure intact.
  * `RENAME` - Renaming a table or column, copying table structure.
* **Data Types & Structure**
  * Data Types & Rows/Columns (INT, VARCHAR, DATE, DECIMAL, BOOLEAN, etc.)
* **Constraints (Data Security Guardrails)**
  * `PRIMARY KEY` - Uniquely identifies each record.
  * `FOREIGN KEY` - Maintains referential integrity between tables.
  * `UNIQUE` - Ensures all values in a column are distinct.
  * `CHECK` - Restricts values based on specific logical conditions.
  * `NOT NULL` - Prevents empty/null entries.

---

## 2. DML (Data Manipulation Language)

*Focus: Managing and altering the actual records/data inside the tables.*

* **CRUD Operations**
  * `INSERT INTO` - Adding new data rows into a table.
  * `UPDATE` - Modifying existing records based on specific conditions.
  * `DELETE` - Removing specific rows from a table based on filters.
* **Structure Operations**
  * `COPY` / `RENAME` / `STRUCTURE` - Copying table structure, renaming.
  * `CHECK CONSTRAINT` - Applying/validating row-level check constraints.

---

## 3. DQL (Data Query Language)

*Focus: Retrieving, filtering, sorting, and analyzing data.*

* **Basic Retrieval & Filtering**
  * `SELECT` & `FROM` - Pulling specific columns from tables.
  * `DISTINCT` - Filtering out duplicate records.
  * `WHERE` clause - Applying strict row-level filters.
  * Logical Operators - `AND`, `OR`, `NOT`.
  * Range & Set Operators - `BETWEEN`, `IN`, `IS NULL`.
  * Pattern Matching - `LIKE` and `ILIKE` (case-insensitive) with wildcards (`%`, `_`).
* **Sorting & Pagination**
  * `ORDER BY` - Sorting results in Ascending (`ASC`) or Descending (`DESC`) order.
  * `LIMIT` & `OFFSET` - Controlling pagination and row display counts.
* **Conditional Logic**
  * `CASE` Statements - Implementing multi-branch conditional logic (`IF-THEN-ELSE`).
  * `COALESCE` - Returns first non-null value from a list.
  * `NULLIF` - Returns NULL if two expressions are equal.
* **Aggregations & Grouping**
  * Aggregate Functions - `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()`.
  * `GROUP BY` - Aggregating rows into logical groups.
  * `HAVING` - Filtering groups after aggregation.
* **Joins (Combining Multiple Tables)**
  * `INNER JOIN` - Matching rows present in both tables.
  * `LEFT JOIN` - All records from the left table, matched with the right.
  * `RIGHT JOIN` - All records from the right table, matched with the left.
  * `FULL OUTER JOIN` - Complete combination of both tables.
  * `CROSS JOIN` - Cartesian product of two tables.
  * `SELF JOIN` - Joining a table to itself for hierarchical evaluations.
  * `UNION` / `UNION ALL` - Combining multiple query result sets.
* **Subqueries**
  * Scalar Subqueries - Single-value returning queries inside another query.
  * Correlated Subqueries / `EXISTS` - Row-by-row dependency checks.
* **String, Date & Time Functions**
  * String Functions - CONCAT, SUBSTRING, UPPER, LOWER, TRIM, LENGTH, etc.
  * Date & Time Functions - NOW, DATEDIFF, DATE_FORMAT, EXTRACT, etc.

---

## 4. TCL (Transaction Control Language)

*Focus: Managing database transactions to ensure data safety and atomicity.*

* `START TRANSACTION` / `BEGIN` - Initiating a safe transaction block.
* `COMMIT` - Saving changes permanently to the database.
* `ROLLBACK` - Reverting changes if an error occurs during execution.
* `SAVEPOINT` - Setting a point within a transaction to roll back to partially.

---

## 5. DCL (Data Control Language)

*Focus: Managing database security, user privileges, and access control.*

* `GRANT` - Giving specific user access permissions (e.g., `SELECT`, `INSERT`).
* `REVOKE` - Removing previously granted access permissions from a user.

---

## 6. Advanced Analytics & Architecture

*Focus: Professional-level performance optimization and deep insights.*

* **Views & Structures**
  * `CREATE VIEW` - Saving complex queries as virtual tables.
  * Temp Tables - Temporary tables for intermediate results.
* **Advanced Querying**
  * CTEs (Common Table Expressions) - Writing clean modular queries using the `WITH` clause.
* **Window Functions & Partitioning**
  * Ranking Functions - `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`.
  * Partitioning - `PARTITION BY` logic.
  * Value Functions - `LEAD()` and `LAG()`.
* **Automation & Reusable Logic**
  * Functions & Triggers - Auto-run logic on data changes.
  * Stored Procedures - Reusable blocks of SQL logic.
* **Performance Optimization**
  * Indexes - Creating indexes (`CREATE INDEX`) for high-speed searches.
  * Query Analysis - Using `EXPLAIN` execution plans and query analysis techniques to measure performance.
