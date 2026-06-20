# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC   category AS product,
# MAGIC   SUM(revenue) AS total_revenue
# MAGIC FROM gold_sales_category
# MAGIC GROUP BY category
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 5;
# MAGIC
# MAGIC SELECT
# MAGIC   region,
# MAGIC   SUM(revenue) AS total_revenue
# MAGIC FROM gold_sales_region
# MAGIC GROUP BY region
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 1;
# MAGIC
# MAGIC WITH monthly AS (
# MAGIC   SELECT
# MAGIC     DATE_FORMAT(date, 'yyyy-MM') AS month,
# MAGIC     SUM(revenue) AS monthly_revenue
# MAGIC   FROM gold_sales_daily
# MAGIC   GROUP BY DATE_FORMAT(date, 'yyyy-MM')
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC   month,
# MAGIC   monthly_revenue,
# MAGIC   LAG(monthly_revenue) OVER (ORDER BY month) AS prev_month_revenue,
# MAGIC   monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month) AS mom_change
# MAGIC FROM monthly
# MAGIC ORDER BY month;
# MAGIC
# MAGIC SELECT
# MAGIC   date,
# MAGIC   revenue,
# MAGIC   SUM(revenue) OVER (ORDER BY date) AS running_total
# MAGIC FROM gold_sales_daily
# MAGIC ORDER BY date;