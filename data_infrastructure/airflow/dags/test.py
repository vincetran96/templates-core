"""Test DAG
"""
from datetime import datetime

from airflow import models
from airflow.models.connection import Connection
from airflow.settings import Session
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.decorators import task, task_group


PG_CONNECTION_ID = "postgres"
PG_HOST = "onprem_postgresdb"
PG_USERNAME = "postgres"
PG_PASSWORD = "123"
PG_DB_NAME = "crypto_trading"
PG_PORT = "5432"


with models.DAG(
    dag_id="test_dag",
    schedule="@once",
    start_date=datetime(2023, 11, 24),
    catchup=False,
    tags=["postgres"],
) as dag:
    @task(task_id="setup_postgres_conn")
    def task_postgres_conn():
        """Task to setup
        """
        connection = Connection(
            conn_id=PG_CONNECTION_ID,
            conn_type="postgres",
            host=PG_HOST,
            login=PG_USERNAME,
            password=PG_PASSWORD,
            schema=PG_DB_NAME,
            port=PG_PORT
        )
        with Session() as session:
            if session.query(Connection).filter(
                Connection.conn_id == PG_CONNECTION_ID
            ).first():
                print("Connection already exists")
            else:
                session.add(connection)
                session.commit()

    postgres_conn = task_postgres_conn()

    SQL_QUERY = """
        SELECT user_id, symbol, position, last_updated
        FROM public.user_position
        WHERE last_updated = '2023-10-28'
    """

    task_query = SQLExecuteQueryOperator(
        task_id="sql_query",
        conn_id=PG_CONNECTION_ID,
        sql=SQL_QUERY,
    )

    postgres_conn >> task_query
