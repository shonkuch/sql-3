Data flow and architecture:

Raw files (ingests) are introduced into bronze
Bronze layer handles deduplication and removes stale data (old dates)
Silver layer handles validation logic
Finally, gold layers run analysis and collect data to be used in analytics and dashboards

Data quality rules:
I deduplicate, check ingestion dates
Data rules:
`Sales` >= 0
  AND `Quantity` > 0
  AND `Ship Date` >= `Order Date`

Assumptions:
Tables are preinitialized; data contains required fields in parseable format

Limitations:
Flow depends on initialization done correctly + somewhat reliable data. Bronze layer should be much more resilent for production system


