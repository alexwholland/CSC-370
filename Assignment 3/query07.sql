-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

-- 12 Golf Operators
SELECT 
    name, 
    c1.population AS '2010', 
    c2.population AS '2019', 
    abbr, 
    ((c1.population-c2.population)/c1.population)*100 AS 'Loss (%)'
FROM countypopulation c1
	LEFT JOIN countypopulation c2 ON c1.county = c2.county
    JOIN county ON c1.county = fips
    JOIN state ON state = id
WHERE c1.year = 2010 AND c2.year = 2019 
ORDER BY `Loss (%)` DESC
LIMIT 1
