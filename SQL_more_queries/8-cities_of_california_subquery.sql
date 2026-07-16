-- Lists all cities of California using a subquery (no JOIN), sorted by id
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
