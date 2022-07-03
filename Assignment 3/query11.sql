-- Retrieve alphabetically the states that had
-- over 100 counties with unemployment rates above 6.0%
-- in 2008.
-- Hint: Unemployment rate = unemployed / labour force
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer


-- This method uses implicit Join syntax (not recommended)
-- 6 Golf Operators
SELECT DISTINCT 
    s.abbr
FROM county c, countylabourstats cls, state s
WHERE c.fips = cls.county
    AND c.state = s.id
    AND (cls.unemployed / cls.labour_force) > 0.06
    AND cls.year = 2008
GROUP BY c.state
HAVING COUNT(c.state) > 100
ORDER BY s.abbr;


-- Original solution (recommended)
-- 8 Golf Operators
-- SELECT DISTINCT 
--     s.abbr
-- FROM county c
-- JOIN countylabourstats cls ON cls.county = c.fips
-- JOIN state s ON s.id = c.state
-- WHERE (cls.unemployed / cls.labour_force) > 0.06
--     AND cls.year = 2008
-- GROUP BY c.state
-- HAVING COUNT(c.state) > 100
-- ORDER BY s.abbr;
