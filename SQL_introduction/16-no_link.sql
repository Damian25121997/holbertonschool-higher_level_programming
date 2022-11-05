-- List all records of the table of the database in MySQL server.
SELECT score, name
FROM second_table
WHERE `name` IS NOT NULL AND score >= 10
ORDER BY score DESC;
