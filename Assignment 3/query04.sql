-- Retrieve alphabetically all states in which
-- every county has a name not found anywhere else
-- in the US
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer

-- 8 Golf Operators 
SELECT s.abbr
FROM state s
WHERE s.id NOT IN(
	SELECT c1.state
	FROM county c1, county c2
	WHERE c1.fips <> c2.fips
	AND c1.name = c2.name)
ORDER BY s.abbr;
