from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task-Funktion
def hello_airflow():
    print("Hello, Airflow!")

# DAG-Definition
with DAG(
    dag_id="my_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["example"]
) as dag:

    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=hello_airflow
    )

    # Wenn du mehrere Tasks hättest, könntest du hier die Reihenfolge festlegen:
    # task1 >> task2