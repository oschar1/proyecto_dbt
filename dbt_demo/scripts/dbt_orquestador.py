from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def mi_funcion_tarea():
    subprocess.run(
        ["dbt", "run", "--select", "orders"],
        check=True
    )



    from datetime import datetime, timedelta
import subprocess

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def ejecutar_dbt():
    subprocess.run(
        ["dbt", "run", "--select", "orders"],
        check=True
    )


with DAG(
    dag_id="ejecutar_orders",
    start_date=datetime(2026, 1, 1),
    schedule="*/2 * * * *",   # cada 2 minutos
    catchup=False,
    tags=["dbt"]
) as dag:

    tarea_orders = PythonOperator(
        task_id="run_orders",
        python_callable=ejecutar_dbt
    )