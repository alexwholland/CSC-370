-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer


-- 22 Golf Operators 

SELECT 
    N.name, 
    N.2010, 
    N.population AS '2019', 
    N.abbr, 
    ABS(MIN(N.Percentage)) AS 'Loss (%)'
FROM(
    SELECT 
    *, 
    (N.population - LAG(N.population, 1) 
    OVER (PARTITION BY N.fips)) / LAG(N.population, 1) 
    OVER (PARTITION BY N.fips) * 100 AS 'Percentage', 
    LAG(N.population, 1) 
    OVER (PARTITION BY N.fips) AS '2010'
    FROM(
        SELECT * 
        FROM county c 
        JOIN state s ON s.id = c.state 
        JOIN countypopulation p ON p.county = c.fips
        WHERE p.year = 2010 OR p.year = 2019
    ) AS N
    ORDER BY Percentage ASC
) AS N
WHERE N.Percentage = (SELECT(MIN(N.Percentage)))
LIMIT 1 OFFSET 1;

WHERE N.Percentage = (SELECT(MIN(N.Percentage)))
