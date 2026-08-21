-- ====================================================================
-- SQL JOINS PRACTICE & EXPLANATIONS
-- ====================================================================


-- ====================================================================
-- 1. INNER JOIN
-- ====================================================================
-- Explanation: Yeh query employees aur departments tables ko aapas mein 
-- jodti hai. Yeh sirf wahi rows return karegi jinka department_id 
-- dono tables mein match hota hai. Jinka match nahi hoga, wo gayab ho jayenge.

SELECT e.*
FROM employees AS e
    INNER JOIN departments AS d ON e.department_id = d.department_id;


-- ====================================================================
-- 2. LEFT JOIN
-- ====================================================================
-- Explanation: Yeh left table (employees) ka saara data laata hai, aur right 
-- table (departments) se matching data laata hai. Agar kisi employee ka 
-- department match nahi hua, toh department fields ki jagah NULL aa jayega.

SELECT e.*,
    d.dep_name
FROM employees AS e
    LEFT JOIN departments AS d ON e.department_id = d.department_id;


-- ====================================================================
-- 3. RIGHT JOIN
-- ====================================================================
-- Explanation: Yeh right table (departments) ka saara data laata hai, aur left 
-- table (employees) se matching data laata hai. Agar kisi department mein 
-- koi employee nahi hai, toh employee side par NULL show hoga.

SELECT e.*,
    d.dep_name
FROM employees AS e
    RIGHT JOIN departments AS d ON e.department_id = d.department_id;


-- ====================================================================
-- 4. FULL OUTER JOIN (MySQL Emulation)
-- ====================================================================
-- Explanation: Kyunki MySQL mein direct FULL OUTER JOIN keyword support nahi 
-- karta, isliye hum LEFT JOIN aur RIGHT JOIN ko `UNION ALL` ke sath combine 
-- karte hain taaki dono tables ka sara data (matches + unmatches) mil sake.

SELECT e.*,
    d.*
FROM employees AS e
    LEFT JOIN departments AS d ON e.department_id = d.department_id
UNION ALL
SELECT e.*,
    d.*
FROM employees AS e
    RIGHT JOIN departments AS d ON e.department_id = d.department_id
WHERE e.department_id IS NULL;


-- ====================================================================
-- 5. CROSS JOIN
-- ====================================================================
-- Explanation: Yeh Cartesian product banata hai—yani employees table ki har 
-- ek row departments table ki har ek row ke sath combine hoti hai 
-- (Total rows = Employees count × Departments count).

SELECT e.* 
FROM employees AS e
CROSS JOIN departments AS d;


-- ====================================================================
-- 6. SELF JOIN
-- ====================================================================
-- Explanation: Jab ek hi table ko khud ke sath join kiya jata hai. Yahan 
-- humne employees table ko do baar (`e` aur `d`) use kiya hai taaki un 
-- employees ki pairs nikal sakein jo same department mein kaam karte hain. 
-- `e.emp_id < d.emp_id` lagane se duplicate ya ulte pairs nahi aate.

SELECT e.emp_id AS employee_id_1,
       e.first_name AS employee_name_1,
       d.emp_id AS employee_id_2,
       d.first_name AS employee_name_2,
       e.department_id
FROM employees AS e
JOIN employees AS d ON e.department_id = d.department_id
WHERE e.emp_id < d.emp_id;