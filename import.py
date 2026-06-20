# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE bronze_orders
# MAGIC USING DELTA
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC )
# MAGIC AS
# MAGIC SELECT 
# MAGIC     *,
# MAGIC     current_timestamp() AS ingestion_timestamp,
# MAGIC     input_file_name() AS source_file_name
# MAGIC FROM bronze_orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronze_orders