SELECT a.actor_id, a.first_name, a.last_name, a.last_update FROM sakila.actor a
;


SELECT i.inventory_id, i.film_id, i.store_id, i.last_update FROM sakila.inventory i
;

SELECT
	a.address_id,
	a.address,
	a.address2,
	a.district,
	a.city_id,
	a.postal_code,
	a.phone,
	a.location,
	a.last_update
FROM sakila.address a
;


INSERT INTO sakila.address_copy (
																address_id,
																address,
																address2,
																district,
																city_id,
																postal_code,
																phone,
																location,
																last_update)
SELECT
	a.address_id,
	a.address,
	a.address2,
	a.district,
	a.city_id,
	a.postal_code,
	a.phone,
	a.location,
	a.last_update
FROM sakila.address a
;

CREATE TABLE sakila.address_copy (
	address_id  SMALLINT(5) UNSIGNED AUTO_INCREMENT
		PRIMARY KEY,
	address     VARCHAR(50)                         NOT NULL,
	address2    VARCHAR(50)                         NULL,
	district    VARCHAR(20)                         NOT NULL,
	city_id     SMALLINT(5) UNSIGNED                NOT NULL,
	postal_code VARCHAR(10)                         NULL,
	phone       VARCHAR(20)                         NOT NULL,
	location    GEOMETRY                            NOT NULL,
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT fk_address2_city
		FOREIGN KEY (city_id) REFERENCES city (city_id)
			ON UPDATE CASCADE
)
	CHARSET = utf8
;

CREATE INDEX idx_fk_city_id
	ON sakila.address_copy (city_id)
;

CREATE SPATIAL INDEX idx_location
	ON sakila.address_copy (location)
;

