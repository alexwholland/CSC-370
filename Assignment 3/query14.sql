-- Out of those counties with at least 25000 residents,
-- retrieve the pair from the same state
-- that had the absolute closest
-- population in 2018
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

-- 13 Golf Operators 
WITH Q AS(
SELECT *
FROM 
    countypopulation cp, 
    county c, 
    state s
WHERE cp.county = c.fips
    AND c.state = s.id 
    AND cp.year = 2018
    AND cp.population >= 25000 
    )
SELECT 
    b.name, 
    b.population, 
    a.name, 
    a.population
FROM Q a
	JOIN Q b ON a.county <> b.county AND a.state = b.state
ORDER BY ABS(a.population - b.population)
LIMIT 1;
