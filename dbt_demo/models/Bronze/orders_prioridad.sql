
{{ config(materialized='table') }}
--no olvidar de declarar la variable parametro.
{% set prioridades = var('prioridades') %}

SELECT
    O_ORDERDATE,
    {% for prioridad in prioridades %}
    sum(CASE WHEN O_ORDERPRIORITY = '{{ prioridad }}' THEN 1 ELSE 0 END) AS "{{ prioridad }}",
    {% endfor %}
    count(O_ORDERPRIORITY) AS total_
FROM
    SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.ORDERS
GROUP BY
    O_ORDERDATE


    /** el llamado se realizo asi:
    dbt run --select orders_prioridad --vars "prioridades: ['2-HIGH', '3-MEDIUM', '1-URGENT', '5-LOW', '4-NOT SPECIFIED']"
    /