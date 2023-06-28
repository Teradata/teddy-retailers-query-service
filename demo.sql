-- Database and Table creation
CREATE DATABASE qs_demo
AS PERMANENT = 110e6;

CREATE TABLE qs_demo.tvl
(
  customer_id integer,
  email varchar(64),
  bought_items integer,
  tlv integer,
  last_ordered date
)
NO PRIMARY INDEX;

-- customer_tlv.csv

INSERT INTO qs_demo.tvl
SELECT TOP 500 customer_id,
	email,
	bought_items,
	tlv,
	last_ordered
FROM
	(
	LOCATION = '/gs/storage.googleapis.com/clearscape_analytics_demo_data/DEMO_dbtAdvanced/customers_tlv.csv'
) AS d;