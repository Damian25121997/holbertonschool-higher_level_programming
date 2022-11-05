-- List all records of the table of the database in MySQL server.
INSERT INTO second_table (name, score)
VALUES ('Aria', 18);
INSERT INTO second_table (name, score)
VALUES ('Aria', 12);
SELECT score, name
FROM second_table
WHERE `name` IS NOT NULL AND score >= 10
ORDER BY score DESC;
