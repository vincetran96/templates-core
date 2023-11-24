"""Test DAG file
"""
from airflow.models.connection import Connection
from airflow.settings import Session


PG_CONNECTION_ID = "postgres"
PG_HOST = "localhost"
PG_USERNAME = "postgres"
PG_PASSWORD = "123"
PG_DB_NAME = "crypto_trading"
PG_PORT = "5432"


def main():
    """Main program"""
    connection = Connection(
        conn_id=PG_CONNECTION_ID,
        conn_type="postgres",
        host=PG_HOST,
        login=PG_USERNAME,
        password=PG_PASSWORD,
        schema=PG_DB_NAME,
        port=PG_PORT
    )
    session = Session()
    if session.query(Connection).filter(
        Connection.conn_id == PG_CONNECTION_ID
    ).first():
        print("Connection already exists")
    else:
        print("Added a new connection")
        session.add(connection)
        session.commit()


if __name__ == "__main__":
    main()
