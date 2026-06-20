# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC
# MAGIC CREATE or replace TABLE silver_orders 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC WITH 
# MAGIC deduped 
# MAGIC AS 
# MAGIC (
# MAGIC     SELECT *,
# MAGIC     ROW_NUMBER() OVER (
# MAGIC         PARTITION BY `Order ID`
# MAGIC         ORDER BY `Order Date` DESC
# MAGIC         ) AS row_number
# MAGIC     FROM bronze_orders
# MAGIC ),
# MAGIC cleaned AS (
# MAGIC     SELECT
# MAGIC         `Order ID`,
# MAGIC         lower(trim(`Customer Name`)) AS `Customer Name`,
# MAGIC         lower(trim(`Product Name`)) AS `Product Name`,
# MAGIC         `Quantity`,
# MAGIC         `Sales`,
# MAGIC         `Order Date`,
# MAGIC         `Ship Date`,
# MAGIC         `Region`,
# MAGIC         `Category`,
# MAGIC         ingestion_timestamp
# MAGIC     FROM deduped
# MAGIC     WHERE row_number = 1
# MAGIC )
# MAGIC SELECT *
# MAGIC FROM cleaned
# MAGIC WHERE `Sales` >= 0
# MAGIC   AND `Quantity` > 0
# MAGIC   AND `Ship Date` >= `Order Date`;
# MAGIC
# MAGIC   

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE silver_rejected_orders 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC WITH 
# MAGIC deduped 
# MAGIC AS 
# MAGIC (
# MAGIC     SELECT *,
# MAGIC     ROW_NUMBER() OVER (
# MAGIC         PARTITION BY `Order ID`
# MAGIC         ORDER BY `Order Date` DESC
# MAGIC         ) AS row_number
# MAGIC     FROM bronze_orders
# MAGIC ),
# MAGIC cleaned AS (
# MAGIC     SELECT
# MAGIC         `Order ID`,
# MAGIC         lower(trim(`Customer Name`)) AS customer_name,
# MAGIC         lower(trim(`Product Name`)) AS product_name,
# MAGIC         `Quantity`,
# MAGIC         `Sales`,
# MAGIC         `Order Date`,
# MAGIC         `Ship Date`,
# MAGIC         ingestion_timestamp
# MAGIC     FROM deduped
# MAGIC     WHERE row_number = 1
# MAGIC )
# MAGIC SELECT *
# MAGIC FROM cleaned
# MAGIC WHERE NOT (
# MAGIC     `Sales` >= 0
# MAGIC   AND `Quantity` > 0
# MAGIC   AND `Ship Date` >= `Order Date`
# MAGIC );