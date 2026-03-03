
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="data_analytics_transformation_pipeline",
    start_date=datetime(2026,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    task = BashOperator(
        task_id="print_hello",
        bash_command="echo Hello Data Platform"
    )
