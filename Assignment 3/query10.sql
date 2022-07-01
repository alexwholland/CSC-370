-- Retrieve the largest labour force in a
-- single county
-- 1.1 marks: <2 operators
-- 1.0 marks: <3 operators
-- 0.9 marks: <5 operators
-- 0.8 marks: correct answer

-- Solution #2
-- 2 Operators 
SELECT MAX(`labour_force`) AS `MaxLabourForce`
FROM `countylabourstats`;

-- Solution #2
-- SELECT `labour_force` AS `MaxLabourForce `FROM `countylabourstats`
    -- ORDER BY `labour_force` DESC
    -- LIMIT 1;
