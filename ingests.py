# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC WITH source_data AS (
# MAGIC     SELECT *
# MAGIC     FROM bronze_orders
# MAGIC     WHERE ingestion_timestamp > (SELECT MAX(ingestion_timestamp) FROM silver_orders)
# MAGIC ),
# MAGIC deduped AS (
# MAGIC     SELECT *,
# MAGIC            ROW_NUMBER() OVER (
# MAGIC                PARTITION BY `Order ID`
# MAGIC                ORDER BY ingestion_timestamp DESC
# MAGIC            ) AS row_number
# MAGIC     FROM source_data
# MAGIC )
# MAGIC MERGE INTO silver_orders AS target
# MAGIC USING (
# MAGIC     SELECT *
# MAGIC     FROM deduped
# MAGIC     WHERE row_number = 1
# MAGIC ) AS source
# MAGIC ON target.`Order ID` = source.`Order ID`
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *