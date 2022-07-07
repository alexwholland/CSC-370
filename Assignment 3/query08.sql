-- Retrieve the fifteen counties with the largest 2016 vote imbalance,
-- with their vote counts and states, restricted to counties with at least 10000 votes
-- Hint: Use pq to measure variance/imbalance in this question,
-- where p is the probability of voting democrat and q, republican.
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <15 operators
-- 0.8 marks: correct answer

-- 11 Golf Operators
SELECT 
    c.name,
    s.abbr,
    er.dem,
    er.gop,
    er.total_votes
FROM county c
JOIN electionresult er ON c.fips = er.county
JOIN state s ON s.id = c.state
WHERE er.year = 2016 AND er.total_votes >= 10000
ORDER BY (er.dem / er.total_votes) * (er.gop / er.total_votes)
LIMIT 15;
