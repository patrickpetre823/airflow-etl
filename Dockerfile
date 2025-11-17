FROM apache/airflow:3.1.3
ADD requirements.txt .
RUN pip install apache-airflow==3.1.3 -r requirements.txt
