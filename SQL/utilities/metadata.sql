# Schema Sizes
SELECT
	table_schema                                                   AS "DB Name",
	ENGINE,
	ROUND(SUM(data_length + index_length) / 1024 / 1024, 0)        AS "DB Size in MB",
	ROUND(SUM(data_length + index_length) / 1024 / 1024 / 1024, 2) AS "DB Size in GB"
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'insights'
GROUP BY 1
			 , 2
ORDER BY 3 DESC
;

# Engines per Table
SELECT
	TABLE_SCHEMA,
	TABLE_NAME,
	ENGINE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA IN (
		# 		'db_youfilter', 'statistics',
		'insights')
ORDER BY 1
			 , 2
;

DESCRIBE statistics.by_domainid_and_day
;

SELECT *
FROM information_schema.TABLE_CONSTRAINTS
LIMIT 5
;

# Find free space
SELECT
	table_name,
	engine,
	round(data_length / 1024 / 1024) AS data_length_mb,
	round(data_free / 1024 / 1024)   AS data_free_mb
FROM information_schema.tables
WHERE table_name LIKE 'f_g%'
;