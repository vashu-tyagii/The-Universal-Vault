# SQL Revision Sheet — Topics Covered So Far
(Basics → WHERE/Filtering → DDL → DML → JOINs → GROUP BY & HAVING)

Use your `company_db` (employees + departments tables). No hints, no notes — 
if you get stuck, that's the exact topic to revisit before moving forward.

---

## Round 1 — Basics & Filtering (Quick Fire)

1. Select all employees earning more than 35000.
2. Select distinct department_ids from employees.
3. List employees sorted by salary, highest to lowest.
4. Show only the 3 most recently hired employees.
5. Find employees whose email contains "gmail".
6. Find employees NOT in department_id 1.
7. Label each employee "High Salary" (>40000) or "Standard" using CASE.
8. Find employees with a NULL value in any column (pick a column to test).

---

## Round 2 — DDL & DML (Structure + Data)

9. Create a new table `projects` with: project_id (PK), project_name, department_id (FK to departments), budget (DECIMAL).
10. Add a CHECK constraint ensuring budget is always positive.
11. Insert 3 rows into `projects`.
12. Update one project's budget by increasing it 15%.
13. Delete one project by project_id.
14. Add a new column `status` (VARCHAR) to `projects`, then drop it again.

---

## Round 3 — JOINs (Mixed)

15. INNER JOIN employees and departments — show employee name + department name.
16. LEFT JOIN — show ALL employees even if their department doesn't exist in departments.
17. Find departments that have NO employees (use LEFT JOIN + WHERE IS NULL).
18. SELF JOIN — find pairs of employees in the same department.
19. JOIN employees, departments, and projects together — show employee name, department name, and project name (3-table join).

---

## Round 4 — GROUP BY & HAVING (Your Newest Topic — Test It Hard)

20. Total salary paid per department.
21. Average salary per department, rounded to 2 decimal places.
22. Count of employees per department.
23. Departments where total salary exceeds 70000 (HAVING).
24. Departments with more than 2 employees (HAVING).
25. Highest-paid employee in each department (hint: think GROUP BY + subquery, or you'll learn a cleaner way with window functions later).
26. Find the department with the lowest average salary.
27. Count how many employees earn above 35000, grouped by department.

---

## Round 5 — Full Pipeline (Combine Everything — The Real Test)

28. JOIN employees + departments, GROUP BY department, HAVING avg salary > 35000, ORDER BY total salary DESC.
29. Find departments where the employee count is above average department employee count (this needs a subquery + GROUP BY together — attempt it, it's meant to stretch you).
30. Full report: department name, employee count, total salary, average salary — one single query, sorted by total salary descending.

---

## Self-Check — After Finishing

Go back and mark which ones you solved WITHOUT looking anything up:
- [ ] Round 1 (Basics) — solved cleanly?
- [ ] Round 2 (DDL/DML) — solved cleanly?
- [ ] Round 3 (JOINs) — solved cleanly?
- [ ] Round 4 (GROUP BY/HAVING) — solved cleanly?
- [ ] Round 5 (Full Pipeline) — solved cleanly?

Any round where you needed to check notes more than once — that's your revision 
priority before moving to Subqueries (Day 8 in your roadmap).