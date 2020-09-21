SELECT
	min(created_at)                          AS min_date,
	DATE_FORMAT(min(created_at), "%M %D %Y") AS long_date
FROM join_us.users
;

DESC users
;

SELECT email FROM users
WHERE created_at = (SELECT
	min(created_at)                          AS min_date
FROM join_us.users);

SELECT date_format((created_at), "%M") AS month, count(*) AS count
FROM users
GROUP BY 1
ORDER BY 2 DESC
;

SHOW SCHEMAS ;