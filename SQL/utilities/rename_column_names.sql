# Generate alter script(s) to change column names to snake_case
SELECT
	CONCAT('ALTER TABLE ', C.TABLE_NAME, ' CHANGE `', C.COLUMN_NAME, '` ', lower(REPLACE(C.COLUMN_NAME, ' ', '_')), ' ',
				 C.COLUMN_TYPE, ' ', ifnull(C.COLUMN_DEFAULT, 'NULL'), ';') AS alter_text
FROM INFORMATION_SCHEMA.COLUMNS C
WHERE C.TABLE_NAME = 'attributes_campaign'
	AND C.COLUMN_NAME LIKE '% %'
;


SELECT *
FROM information_schema.COLUMNS
WHERE COLUMNS.TABLE_NAME = 'attributes_campaign'

;

SELECT
	attributes_campaign.`Campaign Budget`
FROM insights.attributes_campaign
;


ALTER TABLE attributes_campaign
	CHANGE `Campaign Name` campaign_name VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Tenant` campaign_tenant VARCHAR(150) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Status` campaign_status VARCHAR(14) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Startdate` campaign_startdate VARCHAR(10) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Planner` campaign_planner VARCHAR(342) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Enddate` campaign_enddate VARCHAR(10) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Pricing Model` pricing_model VARCHAR(17) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Budget` campaign_budget DOUBLE(17, 0) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Budget (Original)` campaign_budget_original LONGTEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Price Per Transaction` price_per_transaction VARCHAR(19) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Inheritance` campaign_inheritance TEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Autoboost` campaign_autoboost TEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Retargeting Flag` campaign_retargeting_flag TEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Fixed Flag` campaign_fixed_flag TEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Grayarea Flag` campaign_grayarea_flag INT(1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Closedround Flag` campaign_closedround_flag TINYINT(1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign DCO Flag` campaign_dco_flag INT(1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign SSP Flag` campaign_ssp_flag INT(1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Mobile Flag` campaign_mobile_flag VARCHAR(6)
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign PCD Flag` campaign_pcd_flag MEDIUMTEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign GroupM Flag` campaign_groupm_flag INT(1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Product` campaign_product VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Product Family` campaign_product_family VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Product Parsing` campaign_product_parsing TEXT NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Satellite` campaign_satellite VARCHAR(150) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Manager` campaign_manager VARCHAR(128) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Price Index` campaign_price_index DOUBLE(18, 1) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account ID` account_id VARCHAR(13) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account Name` account_name VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account Group` account_group VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Category CRM` category_crm VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account Address` account_address VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Campaign Owner Sales` campaign_owner_sales VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Advertiser Type` advertiser_type VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account Country` account_country VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account Region` account_region VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account City` account_city VARCHAR(255) NULL
;

ALTER TABLE attributes_campaign
	CHANGE `Account ZIP` account_zip VARCHAR(255) NULL
;


