#FROM apache/airflow:3.1.0
#ADD requirements.txt .
#RUN pip install apache-airflow==3.1.0 -r requirements.txt


FROM apache/airflow:3.1.0

USER root
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
USER airflow
