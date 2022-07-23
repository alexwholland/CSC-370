-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer

-- Source: https://tinyurl.com/3294nfsm
-- 7 Golf Operators 
SELECT 
    (SUM(FmoreThanM = 'yes') / 
    (SUM(FmoreThanM = 'yes') + SUM(FmoreThanM = 'no'))) AS Fraction
FROM (
    SELECT 
        gba.county,
        CASE WHEN gba.population > gbb.population
            THEN 'yes' 
            ELSE 'no' 
            END AS FmoreThanM
    FROM 
        genderbreakdown gba, 
        genderbreakdown gbb
    WHERE gba.county = gbb.county
    AND gbb.gender = 'male'
    AND gba.gender = 'female'
) AS Q;
