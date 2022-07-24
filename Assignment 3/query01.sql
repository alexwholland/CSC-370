-- Retrieve the state with the median number of
-- employees in 'Education Services'
-- 1.1 marks: < 10 operators
-- 1.0 marks: < 11 operators
-- 0.8 marks: correct answer

-- 11 Golf Operators
SELECT 
    s.abbr,
    SUM(
        (SELECT SUM(ci.employees) 
        FROM countyindustries ci, industry i
        WHERE ci.industry = i.id 
        AND ci.county = c.fips
        AND i.name = 'Educational Services')
    ) AS EC
FROM state s
JOIN county c ON s.id = c.state
GROUP BY s.abbr
ORDER BY EC ASC
LIMIT 1 OFFSET 25;
