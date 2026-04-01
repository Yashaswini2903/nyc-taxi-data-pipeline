from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def run_pipeline():
    print("Running batch job...")

default_args = {
    'start_date': datetime(2024, 1, 1)
}

dag = DAG('nyc_taxi_pipeline', schedule_interval='@monthly', default_args=default_args)

task = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_pipeline,
    dag=dag
)
