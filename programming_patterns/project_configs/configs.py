'''Template for creating project configs
'''
import os
from enum import Enum


class OsVar(Enum):
    '''OS variables
    '''
    CURRENT_USER_HOME = "HOME"
    DBHOST = "DBHOST"


class AirflowVar(Enum):
    '''Airflow variables
    '''
    DB_INTERFACE = "DB_INTERFACE"


class Configs:
    '''Class to get config variables
    '''
    @classmethod
    def get_os_var(cls, var: str):
        '''Gets OS variable
        '''
        return os.getenv(var)

    @classmethod
    def get_airflow_var(cls, var: str):
        '''Gets Airflow variable
        '''
        return os.getenv(var)


if __name__ == "__main__":
    print(Configs.get_os_var(OsVar.CURRENT_USER_HOME.value))
