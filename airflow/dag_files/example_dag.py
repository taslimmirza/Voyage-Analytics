from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def my_task():
    # Task to run
    print("Running my task")

dag = DAG('my_dag', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    dag=dag,
)
