-- Retrieve alphabetically the names of industries that
-- employ at least ten million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

-- 12 Golf Operators
SELECT i.name
FROM 
    countyindustries ci, 
    industry i
WHERE 
    ci.industry = i.id 
    AND ci.county NOT IN (
	    SELECT c.fips
	    FROM county c, state s
        WHERE s.id = c.state
        AND s.abbr = 'CA'
    )
GROUP BY ci.industry
HAVING SUM(ci.employees) >= 5000000
ORDER BY i.name;
