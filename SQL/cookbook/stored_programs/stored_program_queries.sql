CREATE PROCEDURE show_part_of_day()
BEGIN
	DECLARE cur_time , day_part TEXT; SET cur_time = CURTIME();
	IF cur_time < '12:00:00' THEN
		SET day_part = 'morning' ;
		ELSEIF cur_time = '12:00:00' THEN
			SET day_part = 'noon' ; ELSE
		SET day_part = 'afternoon or night' ;
		END IF;
	SELECT cur_time, day_part;
END
;

CALL show_part_of_day()
;


# Triggers for logging changes

CREATE TABLE auction (
	id   INT UNSIGNED   NOT NULL AUTO_INCREMENT,
	ts   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	item VARCHAR(30)    NOT NULL,
	bid  DECIMAL(10, 2) NOT NULL,
	PRIMARY KEY (id)
)
;

CREATE TABLE auction_log (
	action ENUM ( 'create' , 'update' , 'delete' ),
	id     INT UNSIGNED   NOT NULL,
	ts     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	item   VARCHAR(30)    NOT NULL,
	bid    DECIMAL(10, 2) NOT NULL,
	INDEX (id)
)
;