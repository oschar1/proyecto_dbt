{{ config(materialized='table') }}
WITH ORDENES_COMP AS (
select *
from DBT_TEST.DBT_OSCAR.ORDERS_COMPLETAS
)

select *, CURRENT_DATE() AS FechaCarga
FROM ORDENES_COMP