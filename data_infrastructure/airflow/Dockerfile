FROM apache/airflow:2.7.2

USER root

RUN apt-get update && apt-get install -y telnet nano

USER airflow
COPY dags /opt/airflow/dags
COPY py /opt/airflow/py
COPY requirements.txt /opt/airflow

USER airflow
WORKDIR /opt/airflow
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
