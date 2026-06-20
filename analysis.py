# Databricks notebook source
# MAGIC %sql
# MAGIC explain extended
# MAGIC SELECT /*+ BROADCAST(small_table) */
# MAGIC   region,
# MAGIC   SUM(gold_sales_region.revenue) AS total_revenue
# MAGIC FROM gold_sales_region
# MAGIC JOIN gold_sales_daily 
# MAGIC on gold_sales_region.revenue = gold_sales_daily.revenue
# MAGIC GROUP BY region
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 1;