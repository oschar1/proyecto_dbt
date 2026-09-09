{{ config(materialized='table') }}
select
c_customer_sk,
c_customer_id,
c_first_name,
c_last_name
--    id as customer_id,
--    first_name,
--    last_name
from SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CUSTOMER
--FROM {{ source('jaffle_shop', 'customers') }}
