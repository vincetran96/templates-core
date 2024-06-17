"""
    DAG for ETL cohorts by month
"""
import logging
from typing import List

import pendulum
from airflow.decorators import dag, task
from pandas import date_range

from common.alert import airflow_on_failure_callback
from services.etl.etl_manual.etl_manual import run_something


@dag(
    dag_id="etl_cohorts_monthly",
    tags=["etl_manual"],
    start_date=pendulum.datetime(2024, 1, 1, 0, 0, 0, tz="Asia/Ho_Chi_Minh"),
    schedule=None,
    max_active_runs=1,
    catchup=False,
    on_failure_callback=airflow_on_failure_callback,
    render_template_as_native_obj=True
)
def etl_cohorts_monthly():
    """ETL cohorts by month taskflow
    """
    param_path = "{{ params.path }}"
    param_cohorts = "{{ params.cohorts }}"
    param_start_date = "{{ dag_run.conf.get('start_date', dag_run.logical_date.astimezone(dag.timezone) | ds) }}"
    param_end_date = "{{ dag_run.conf.get('end_date', dag_run.logical_date.astimezone(dag.timezone) | ds) }}"

    @task(task_id="run_job")
    def run_job(path: str, cohorts: List[str], start_date: str, end_date: str):
        logging.info(f"date: {start_date}")
        for cohort in cohorts:
            for date in date_range(start=start_date, end=end_date, freq="M"):
                run_something(path=path, cohort=cohort, period=date.strftime("%Y-%m-%d"))

    run_job(
        path=param_path,
        cohorts=param_cohorts,
        start_date=param_start_date,
        end_date=param_end_date
    )


etl_cohorts_monthly()
