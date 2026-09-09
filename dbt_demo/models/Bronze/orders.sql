WITH raw_orders AS (
	SELECT
		O_ORDERKEY as order_id,
		O_ORDERPRIORITY as prioridad,
		O_ORDERDATE as order_date,
		O_ORDERSTATUS as status
	FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.ORDERS
)
SELECT * FROM raw_orders
