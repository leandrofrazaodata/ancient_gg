from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

# This path need adjustment based on the Composer setup
DBT_PROJECT_DIR = '/home/airflow/dags/dbt_project'

@dag(
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['dbt'],
    description='A simple DAG to run dbt models daily'
)
def dbt_daily_run():
    # run all dbt models
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'dbt run --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}'
    )

    # run dbt tests after the models are built
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'dbt test --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}'
    )

    dbt_run >> dbt_test

# Instantiate the DAG
dbt_daily_run_dag = dbt_daily_run()