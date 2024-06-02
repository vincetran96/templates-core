"""Template for creating project configs
"""
import os
from enum import Enum

from airflow.models import Variable


class OsVar(Enum):
    """OS variables
    """
    CURRENT_USER_HOME = "HOME"
    DBHOST = "DBHOST"


class AirflowVar(Enum):
    """Airflow variables
    """
    DB_INTERFACE = "DB_INTERFACE"


class Configs:
    """Class to get config variables
    """
    @staticmethod
    def get_os_var(var: str):
        """Gets OS variable
        """
        return os.getenv(var)

    @staticmethod
    def get_airflow_var(var: str):
        """Gets Airflow variable
        """
        return Variable.get(var)


if __name__ == "__main__":
    print(Configs.get_os_var(OsVar.CURRENT_USER_HOME.value))
