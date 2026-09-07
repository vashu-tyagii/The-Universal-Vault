-- 1. Delimiter change karo taaki compiler beech mein semicolon (;) dekh kar confuse na ho
DELIMITER //

CREATE FUNCTION CalculateBonus(sal DECIMAL(10,2)) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    -- Variable declare karo jisme calculation store hogi
    DECLARE bonus DECIMAL(10,2);
    
    -- Logic: Salary ka 15% bonus nikaalo
    SET bonus = sal * 0.15;
    
    -- Final value return karo
    RETURN bonus;
END //

-- 2. Delimiter ko wapas normal karo
DELIMITER ;

SELECT emp_name, salary, CalculateBonus(salary) AS calculated_bonus
FROM employees;