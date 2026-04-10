from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from jobs.clean_data import clean_data
from jobs.aggregate import aggregate_data

default_args = {
    'owner': 'analytics',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'analytics_pipeline',
    default_args=default_args,
    description='Daily analytics data processing',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

clean_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag,
)

aggregate_task = PythonOperator(
    task_id='aggregate_data',
    python_callable=aggregate_data,
    dag=dag,
)

clean_task >> aggregate_task