-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'ore', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

SELECT 
    c.name,
    s.abbr,
    ci.employees
FROM countyindustries ci
    JOIN industry i ON ci.industry = i.id
    JOIN county c ON ci.county = c.fips
    JOIN state s ON c.state = s.id
WHERE i.name = 'Mining, quarrying, and oil and gas extraction'
    AND (c.name LIKE '%iron%' 
        OR c.name LIKE '%ore%' 
        OR c.name LIKE '%mineral%')
ORDER BY c.snow;
