# Databricks notebook source
# MAGIC %sql
# MAGIC /*Create the following tables:
# MAGIC
# MAGIC gold_sales_daily
# MAGIC | date | revenue |
# MAGIC
# MAGIC gold_sales_region
# MAGIC | region | revenue |
# MAGIC
# MAGIC gold_sales_category
# MAGIC | category | revenue |
# MAGIC
# MAGIC gold_customer_metrics
# MAGIC | customer | revenue | orders |*/
# MAGIC
# MAGIC CREATE or replace TABLE gold_sales_daily 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC SELECT
# MAGIC     date(`Order Date`) AS date,
# MAGIC     sum(`Sales`) AS revenue
# MAGIC FROM silver_orders
# MAGIC GROUP BY date;
# MAGIC
# MAGIC CREATE or replace TABLE gold_sales_region 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC SELECT
# MAGIC     `Region` AS region,
# MAGIC     sum(`Sales`) AS revenue
# MAGIC FROM silver_orders
# MAGIC GROUP BY `Region`;
# MAGIC
# MAGIC CREATE or replace TABLE gold_sales_category 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC SELECT
# MAGIC     `Category` AS category,
# MAGIC     sum(`Sales`) AS revenue
# MAGIC FROM silver_orders
# MAGIC GROUP BY `Category`;
# MAGIC
# MAGIC CREATE or replace TABLE gold_customer_metrics 
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC SELECT
# MAGIC     `Customer Name` AS customer,
# MAGIC     sum(`Sales`) AS revenue,
# MAGIC     count(`Order ID`) AS orders
# MAGIC FROM silver_orders
# MAGIC GROUP BY `Customer Name`;