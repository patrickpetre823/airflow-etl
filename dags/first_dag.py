from airflow import DAG
from time import datetime

default_args= 
with DAG(
    dag_id = 'first_dag',
    description='First Dag, to try out function',
    start_date=datetime(2025, 10, 20, 6),               # Jahr, Monat, Tag, Uhrzeitat
    schedular_interval='@daily'

) as dag:
    pass