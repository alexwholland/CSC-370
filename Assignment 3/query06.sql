-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'coal', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

-- ~44 Golf Operators 
WITH Q1 AS(
    SELECT 
        Q.fips, 
        Q.name AS 'name', 
        Q.abbr, 
        Q.snow, 
        ci.employees
    FROM(
        SELECT 
            c.fips, 
            c.name AS 'name', 
            s.abbr, 
            c.snow 
        FROM 
            county c, 
            state s
        WHERE 
            s.id = c.state
            AND (c.name LIKE 'mineral%' 
            OR c.name LIKE 'coal%' 
            OR c.name LIKE 'iron%')
    ) Q, countyindustries ci, industry i
    WHERE ci.county = Q.fips
        AND i.name = 'Mining, quarrying, and oil and gas extraction'
        AND ci.industry = i.id
), Q2 AS(
    SELECT 
        c.fips, 
        c.name, 
        s.abbr, 
        c.snow, 
        NULL AS 'employees' 
    FROM 
        county c, 
        state s
    WHERE 
        s.id = c.state
        AND (c.name LIKE 'mineral%' 
        OR c.name LIKE 'coal%' 
        OR c.name LIKE 'iron%')
)
SELECT 
    Q.name, 
    Q.abbr, 
    Q.employees
FROM(
    SELECT 
        Q2.name, 
        Q2.abbr, 
        Q2.snow, 
        Q2.employees 
    FROM Q2
    WHERE Q2.fips NOT IN 
        (SELECT Q1.fips FROM Q1)
    UNION
    SELECT 
        Q1.name, 
        Q1.abbr, 
        Q1.snow, 
        Q1.employees 
    FROM Q1
) Q
ORDER BY Q.snow; 
