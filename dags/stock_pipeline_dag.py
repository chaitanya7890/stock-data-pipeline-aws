from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "chaitanya",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

dag = DAG(
    "stock_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

get_data = BashOperator(
    task_id="get_stock_data",
    bash_command="python scripts/get_stock_data.py",
    dag=dag
)

transform = BashOperator(
    task_id="transform_data",
    bash_command="python scripts/transform_data.py",
    dag=dag
)

validate = BashOperator(
    task_id="validate_data",
    bash_command="python scripts/validate_data.py",
    dag=dag
)

upload = BashOperator(
    task_id="upload_to_s3",
    bash_command="python scripts/upload_to_s3.py",
    dag=dag
)

get_data >> transform >> validate >> upload