{{ config(materialized='table') }}
with transformed_orders as (
	select
		order_id,
		DATE_TRUNC('month',order_date) as order_month,
		status
	from {{ref('orders')}}
),

final as (
	SELECT 
		order_month,
		count(order_id) as totclal_orders
	FROM transformed_orders
    --WHERE YEAR(order_month) = 1998
	--AND MONTH(order_month) in (1)
	GROUP BY order_month
	ORDER BY order_month
)

SELECT * FROM final