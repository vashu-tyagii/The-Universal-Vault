# SQL Subquery Practice Bootcamp (70 Questions)

**Database:** `local_db`  
**Tables Available:** `departments`, `employees`, `projects`, `project_assignments`

---

## 🟢 Category 1: Single-Row Subquery (10 Questions)

1. Find the employee(s) who earn the highest salary in the company.
2. Find all employees who earn less than the average salary of the entire company.
3. Find employees who were hired earlier than the employee with `emp_id = 105`.
4. Find the employee(s) who have the exact minimum salary in the company.
5. Find employees whose salary is greater than employee `102`'s salary.
6. Find employees working in the same department as employee `115`.
7. Find employees whose salary is equal to the maximum salary of the company.
8. Find employees who earn more than the employee named 'Vikram' (`first_name = 'Vikram'`).
9. Find employees hired on the exact same date as the earliest hire date in the company.
10. Find employees whose salary is less than the maximum salary in the company.

---

## 🟡 Category 2: Multi-Row Subquery (10 Questions)

1. Find all employees who work in departments located in 'Bangalore', 'Hyderabad', or 'Mumbai'.
2. Find employees whose salaries match the salary of *any* manager in the company (`manager_id IS NULL`).
3. Find employees who do *not* work in the 'Engineering' or 'Finance' departments.
4. Find employees whose salary is greater than *all* salaries of employees in the 'Human Resources' department.
5. Find employees who work in departments that have more than 5 employees.
6. Find employees assigned to projects with a budget greater than 400,000.
7. Find employees whose job roles match any job role in the 'Data Science' department.
8. Find employees who are *not* assigned to any project in the `project_assignments` table (`NOT IN`).
9. Find employees working in departments where the location starts with the letter 'B'.
10. Find employees whose salaries are in the list of top 5 highest salaries in the company.

---

## 🔵 Category 3: Multi-Column Subquery (10 Questions)

1. Find employees who have the minimum salary in their respective departments (`(department_id, salary) IN (...)`).
2. Find employees who have the maximum salary in their respective departments.
3. Find employees whose `department_id` and `salary` match the department and salary of employee `102`.
4. Find employees who share both the same department and same hire date as someone else in the table.
5. Find employees whose `department_id` and `manager_id` combination matches any department's leadership pattern.
6. Find employees whose `emp_id` and `department_id` exist in the project assignments as a valid pair.
7. Find employees whose job role and salary match the lowest paid tier per department.
8. Find employees whose department and salary match the highest paid tier per department.
9. Find employees whose `department_id` and `salary` are equal to any department's average metrics.
10. Find employees who match the department and minimum hire date of that department.

---

## 🟣 Category 4: Correlated Subquery (10 Questions)

1. Find employees whose salary is greater than the average salary of their own department.
2. Find employees whose salary is the maximum in their respective department.
3. Find employees who earn less than the average salary of their department.
4. Find employees who were hired before their department's average hire date.
5. Find employees who earn more than any other employee in a different department.
6. Find managers (`manager_id IS NULL`) who earn more than the average salary of the team members reporting to them.
7. Find employees who have a salary higher than the employee with the lowest salary in the *same* department.
8. Find employees whose salary is equal to the maximum salary in their respective department.
9. Find employees who are the *only* ones earning above 90,000 in their department.
10. Find employees whose employee ID is greater than the average employee ID of their department.
