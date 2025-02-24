import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["patfredsean09@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
    "start_date": datetime.datetime(2024, 10, 7),
}

dag = DAG(
    'fetch_cricket_stats',
    default_args=default_args,
    description='Runs an external Python script',
    schedule_interval='@daily',
    catchup=False
)

with dag:
    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push_gcs.py'
    )