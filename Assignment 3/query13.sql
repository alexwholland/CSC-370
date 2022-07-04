-- Retrieve alphabetically all states
-- with at least one hundred counties.
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

-- 6 Golf Operators
SELECT s.abbr
FROM state s
JOIN county c ON c.state = s.id
GROUP BY c.state
HAVING COUNT(*) >= 100
ORDER BY s.abbr;
