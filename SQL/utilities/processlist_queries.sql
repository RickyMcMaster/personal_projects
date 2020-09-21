SELECT *
	   # 	PROCESSLIST.ID
FROM information_schema.PROCESSLIST
# WHERE PROCESSLIST.USER = 'r_user'
#   AND PROCESSLIST.INFO IS NULL
;

SELECT
	date_sub(current_timestamp, INTERVAL pl.time SECOND) AS ts_start,
	pl.ID,
	pl.USER,
	pl.HOST,
	pl.DB,
	pl.COMMAND,
	pl.TIME,
	pl.STATE,
	pl.INFO,
# 	pl.TIME_MS,
	pl.ROWS_SENT,
	pl.ROWS_EXAMINED
FROM information_schema.PROCESSLIST pl
WHERE TRUE
#   AND pl.USER = 'dgi'
# AND pl.ROWS_EXAMINED > 0
# and pl.COMMAND != 'Sleep'
ORDER BY ts_start DESC
# LIMIT 30
;


SHOW FULL PROCESSLIST;


SHOW GRANTS;

SELECT *
FROM mysql.user u
WHERE u.User = 'rmm'
;

# All my processes
SELECT
	date_sub(current_timestamp, INTERVAL pl.time SECOND) AS ts_start,
	id
FROM information_schema.PROCESSLIST pl
WHERE TRUE
  AND pl.USER = 'dgi'
ORDER BY 1 DESC
;

CALL insights.etl_procedure(yesterday(), yesterday());

SHOW EVENTS;

SELECT *
FROM insights.etl_log_old el
WHERE el.job_rundate = current_date
ORDER BY start_time DESC;
;

SELECT month(day), count(*) FROM insights.f_domain_widget fdw
WHERE fdw.datekey >= 20190101
GROUP BY 1

;


KILL 22972366;
KILL 22972358;
KILL 22972361;
KILL 22972373;
KILL 22972364;
KILL 22972370;
KILL 22972355;
KILL 22972367;
KILL 22972365;
KILL 22972262;
KILL 22972261;
KILL 22972272;
KILL 22972273;
KILL 22972264;
KILL 22972267;
KILL 22972266;
KILL 22972265;
KILL 22972260;
KILL 22972263;
KILL 22972218;

SELECT * FROM insights.d_calendar dc
WHERE dc.current_week = 1
;

