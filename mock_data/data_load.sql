CREATE DATABASE teddy_retailers_warehouse
AS PERMANENT = 110e6;
CREATE TABLE teddy_retailers_warehouse.customers_tlv AS
	(
		SELECT CAST(customer_id as CHAR(5)) as customer_id, email, bought_items, tlv, last_ordered  FROM 
		(
	    	LOCATION='/gs/storage.googleapis.com/clearscape_analytics_demo_data/DEMO_dbtAdvanced/customers_tlv.csv'
		) as d
)  WITH DATA;