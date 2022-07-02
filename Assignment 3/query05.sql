-- Retrieve in descending order of labour force size
-- all counties that had unemployment rates over 10%
-- in the 2008 census.
-- Hint: Unemployment rate = unemployment / labour force
-- 1.1 marks: <9 operators
-- 1.0 marks: <10 operators
-- 1.0 marks: <15 operators
-- 0.8 marks: correct answer

-- This method uses implicit Join syntax (not recommended)
-- 7 Golf Operators
SELECT 
    c.name, 
    s.abbr,
    cls.labour_force,
    (cls.unemployed / cls.labour_force) * 100 
        AS "Unemployment Rate"
FROM county c, countylabourstats cls, state s
WHERE c.fips = cls.county
    AND c.state = s.id
    AND (cls.unemployed / cls.labour_force) > 0.1
    AND cls.year = 2008
ORDER BY cls.labour_force DESC;

-- Original solution (recommended)
-- 9 Golf Operators
-- SELECT 
--     c.name, 
--     s.abbr,
--     cls.labour_force,
--     (cls.unemployed / cls.labour_force) * 100 
--         AS "Unemployment Rate"
-- FROM county c
-- JOIN countylabourstats cls ON cls.county = c.fips
-- JOIN state s ON s.id = c.state
-- WHERE (cls.unemployed / cls.labour_force) > 0.1 
--     AND cls.year = 2008
-- ORDER BY cls.labour_force DESC;
