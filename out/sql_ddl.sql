
CREATE TABLE dim_customer (
	id INTEGER NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50), 
	middle_initial VARCHAR(10), 
	address VARCHAR(100), 
	city VARCHAR(100), 
	state VARCHAR(100), 
	country VARCHAR(100), 
	PRIMARY KEY (id)
)

;

CREATE TABLE dim_discount_type (
	id INTEGER NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	name VARCHAR(20), 
	PRIMARY KEY (id), 
	CONSTRAINT valid_discount_type CHECK (name IN ('N/A', 'EndofYear', 'Repeat Customer', 'Senior Citizen'))
)

;

CREATE TABLE dim_product (
	id INTEGER NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	name VARCHAR(100), 
	description_long TEXT, 
	PRIMARY KEY (id)
)

;

CREATE TABLE fact_customer_relations (
	id INTEGER NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	dim_customer_id INTEGER, 
	encounter_date DATE, 
	encounter_notes TEXT, 
	is_repeat_customer BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dim_customer_id) REFERENCES dim_customer (id)
)

;

CREATE TABLE fact_orders (
	id INTEGER NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	dim_customer_id INTEGER, 
	dim_product_id INTEGER, 
	dim_discount_type_id INTEGER, 
	sale_date DATE, 
	sale_qty DECIMAL, 
	sale_amount DECIMAL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dim_customer_id) REFERENCES dim_customer (id), 
	FOREIGN KEY(dim_product_id) REFERENCES dim_product (id), 
	FOREIGN KEY(dim_discount_type_id) REFERENCES dim_discount_type (id)
)

;
