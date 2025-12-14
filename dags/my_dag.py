from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from traffic_data.fetch_data import fetch_traffic_data

# Task-Funktion
def fetch():
    return fetch_traffic_data()

# DAG-Definition
with DAG(
    dag_id="traffic_api_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@minutely",
    catchup=False,
    tags=["example"]
) as dag:

    fetch_task = PythonOperator(task_id="fetch_data", python_callable=fetch)


    # Wenn du mehrere Tasks hättest, könntest du hier die Reihenfolge festlegen:
    # task1 >> task2