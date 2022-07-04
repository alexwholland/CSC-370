-- Retrieve alphabetically the names of industries that
-- employ at least five million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

-- 7 Golf Operators
SELECT i.name
FROM industry i
WHERE (
    SELECT SUM(s.employees) FROM countyindustries s
    WHERE s.industry = i.id
    AND s.county NOT LIKE '6%'
) >=5000000
ORDER BY i.name ASC;
