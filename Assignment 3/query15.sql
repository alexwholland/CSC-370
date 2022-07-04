-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer

-- 7 Golf Operators 
SELECT 
    (SUM(MoreFemales = 'TRUE') / (SUM(MoreFemales = 'FALSE') 
    + SUM(MoreFemales = 'TRUE'))) AS Fraction
FROM (
    SELECT gba.county,
    CASE WHEN gbb.population < gba.population
    THEN 'TRUE' ELSE 'FALSE' 
    END AS MoreFemales
    FROM genderbreakdown gba
    JOIN genderbreakdown gbb ON gba.county = gbb.county 
    WHERE gba.gender = 'female'
    AND gbb.gender = 'male'
) AS T;
