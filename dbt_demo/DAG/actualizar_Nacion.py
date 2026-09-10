import subprocess
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def ejecutar_nation():
    print(f"Ejecutando nation: {datetime.now()}")

    subprocess.run(
        ["dbt", "run", "--select", "nation"],
        check=True
    )


with DAG(
    dag_id="ejecutar_nation",
    start_date=datetime(2026, 1, 1),
    schedule_interval="*/5 * * * *",
    catchup=False,
    tags=["dbt"]
) as dag:

    tarea_nation = PythonOperator(
        task_id="run_nation",
        python_callable=ejecutar_nation
    )