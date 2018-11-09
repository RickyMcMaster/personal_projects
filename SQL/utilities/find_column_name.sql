# Find column name
SELECT DISTINCT
	COLUMNS.TABLE_SCHEMA,
	TABLE_NAME,
	COLUMNS.COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TRUE AND lower(COLUMN_NAME) LIKE '%account%'
# 		AND lower(COLUMNS.TABLE_NAME) LIKE '%account%')
	AND TABLE_SCHEMA IN(
# 		'db_youfilter',
# 		'statistics',
		'insights'
		)
;

# Find table name
SELECT *
FROM information_schema.TABLES ta
WHERE ta.TABLE_NAME LIKE '%db_buffer%'
;

SELECT *
FROM db_youfilter.itemfilter39083
;

SELECT DISTINCT
	device_type
FROM insights.campaigns
LIMIT 50
;

SELECT *
FROM statistics.mobile_dev_all_campaigns
		# WHERE mobile_device.day >= '2016-01-01'
LIMIT 50
;

SELECT
	max(DAY)
FROM statistics.mobile_device
;