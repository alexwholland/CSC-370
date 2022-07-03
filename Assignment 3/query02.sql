-- Retrieve by life expectancy all
-- counties that have no industry data
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

-- 5 Golf Operators
SELECT c.*
FROM county c
    LEFT JOIN  countyindustries ci ON c.fips = ci.county
WHERE ci.industry is NULL
ORDER BY c.life_expectancy;
