-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

-- 21 Golf Operators
WITH N AS (
	SELECT 
        c.state, 
        SUM(cp.population) AS 'Population' 
    FROM 
        countypopulation cp, 
        county c, 
        state s
    WHERE cp.county = c.fips
        AND c.state = s.id
        AND cp.year = 2019
    GROUP BY c.state
)
SELECT 
    s.abbr, 
    i.name, 
    SUM(ci.payroll) AS 'Total Payrolls', 
    ((SUM(ci.employees) / N.Population) * 100) AS '% of Population' 
FROM 
    countyindustries ci, 
    county c, 
    state s, 
    industry i, 
    N
WHERE ci.county = c.fips
    AND c.state = s.id
    AND ci.industry = i.id
    AND N.state = c.state
    AND s.abbr != 'DC'
GROUP BY c.state, ci.industry
HAVING `% of Population` >= 7.5
ORDER BY `Total Payrolls` DESC;
