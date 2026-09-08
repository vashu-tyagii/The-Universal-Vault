# CTE Practice Questions — 10 Questions

Use your `company_db` (employees, departments tables). Add a `projects` table
if you built one earlier, otherwise questions 8-9 can be adapted to what you have.

Rule: Solve with CTEs specifically — even if you could write it as a subquery,
practice the `WITH ... AS (...)` syntax.

---

1. Write a CTE that selects all employees with salary > 35000, then query the
   CTE to show only their names and salary.

2. Write a CTE that calculates total salary per department, then use it to
   find which department has the highest total salary.

3. Write a CTE that calculates average salary per department, then JOIN it
   back to the employees table to show each employee's salary alongside their
   department's average.

4. Write two CTEs in a single query — one calculating employee count per
   department, another calculating total salary per department — then combine
   both in the final SELECT.

5. Write a CTE that lists departments with more than 2 employees, then JOIN
   it with the departments table to also show department location.

6. Write a CTE to find the top 2 highest earners overall (across all
   departments combined), then display their department names as well.

---

## Self-Check

- [ ] Q1-Q4 (Basic CTE usage) — solved cleanly?
- [ ] Q5-Q6 (CTE + window functions / replacing correlated subqueries) — solved cleanly?
- [ ] Q7-Q9 (CTE + JOIN + HAVING-style filtering) — solved cleanly?
- [ ] Q10 (Recursive CTE) — this one's genuinely hard, don't worry if it takes
      multiple attempts; recursive CTEs trip up experienced people too.
