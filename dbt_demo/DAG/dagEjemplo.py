import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain, cross_downstream


def process_data():
    print("Processing data for the day...")
    # Simulate data processing logic


def generate_report():
    print("Generating the daily report...")
    # Simulate report generation logic


def send_notification():
    print("Sending notification about the report...")
    # Simulate notification logic


# DAG definition
with DAG(
    dag_id="dag_example_1",
    start_date=datetime.datetime(2025, 1, 23),
    schedule_interval="@daily",
    # schedule_interval="30 15 * * 1-5"
    catchup=False,
    default_args={"retries": 2, "retry_delay": datetime.timedelta(minutes=1), "timeout": 300},
    description="A first DAG explaining Airflow Concepts",
) as dag:

    # Tasks
    start_task = BashOperator(
        task_id="start_task",
        bash_command="echo 'Starting the daily workflow'",
    )
	
data_processing_task = PythonOperator(
	task_id="data_processing_task",
	python_callable=process_data,
)

report_generation_task = PythonOperator(
	task_id="report_generation_task",
	python_callable=generate_report,
)	

send_notification_task = PythonOperator(
	task_id="send_notification_task",
	python_callable=send_notification,
)

cleanup_task = BashOperator(
	task_id="cleanup_task",
	bash_command="rm -rf /Users/praveenreddy/Arflw/Data/src/",
)

	# Dependencies

	# Basic chaining
start_task >> data_processing_task
	
# Cross downstream ---> If you want to make a list of tasks depend on another list of tasks
cross_downstream([data_processing_task], [report_generation_task, archive_data_task])

# Chain for complex dependencies
chain(report_generation_task, send_notification_task, cleanup_task)	