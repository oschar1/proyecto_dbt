{{config(materialized='table')}}

select fechacarga-o_orderdate as dias_transcurridos, 
o_orderpriority, 
count(*) as cantidad_ordenes
from DBT_TEST.DBT_OSCAR.ORDER_COMPLETAS_SILVERL
group by 1,2

db