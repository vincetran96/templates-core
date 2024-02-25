"""Passwords and other configs
"""
import sys
import os
from pathlib import Path
from dotenv import dotenv_values


CONFIGS = dotenv_values(Path(__file__).parents[1] / ".env")

CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER') or CONFIGS['USER']
CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD') or CONFIGS['PASSWORD']

# USER_DEV = CONFIGS['USER_DEV']
# PASSWORD_DEV = CONFIGS['PASSWORD_DEV']

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

CH_PROD_HOST = 'https://localhost:443'
CH_DEV_HOST = 'http://localhost:8123'
CH_TIMEDELTA_REQUESTS = 0.5

GPU_HOST = "10.0.8.27" or CONFIGS['GPU_HOST']
GPU_TRAIN_PORT = 8081
# GPU_USERNAME = CONFIGS['GPU_USERNAME']
# GPU_PYENV_PATH = CONFIGS['GPU_PYENV_PATH']
# GPU_SPELLCHECK_PATH = CONFIGS['GPU_SPELLCHECK_PATH']

AIRFLOW_PRIVATE_DATAPATH = "/opt/airflow/data/spellchecker-pipeline"
AIRFLOW_PUBLIC_DATAPATH = "/opt/airflow/data/output/shared/spellchecker-pipeline"

# SLACK_WEBHOOK_URL = "" or CONFIGS['SLACK_WEBHOOK_URL']

LOCAL_TZ = "Asia/Ho_Chi_Minh"
DAY_SECONDS = 86400

WRITE_CHUNKSIZE = 200000
READ_CHUNKSIZE = 1000000
MP_POOL_CHUNKSIZE = 5

PYTHON_EXECUTABLE = sys.executable
