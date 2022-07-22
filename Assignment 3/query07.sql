-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

-- 12 Golf Operators
SELECT 
    name, 
    cpa.population AS '2010', 
    cpb.population AS '2019', 
    abbr, 
    ((cpa.population - cpb.population) / cpa.population) * 100 AS 'Loss (%)'
FROM 
    countypopulation cpa, 
    countypopulation cpb, 
    county c, 
    state s
WHERE 
    cpa.county = cpb.county
    AND cpa.county = c.fips
    AND c.state = s.id
    AND cpa.year = 2010 
    AND cpb.year = 2019 
ORDER BY `Loss (%)` DESC
LIMIT 1;
