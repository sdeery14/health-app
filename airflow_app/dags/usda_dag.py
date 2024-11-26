from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import os

def download_usda_csv():
    url = 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2024-10-31.zip'
    output_dir = '/opt/airflow/data'
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(url)
    with open(f"{output_dir}/FoodData_Central.zip", "wb") as f:
        f.write(response.content)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 31),
    'retries': 1,
}

with DAG('usda_csv_download',
         default_args=default_args,
         schedule_interval=None) as dag:

    task_download_csv = PythonOperator(
        task_id='download_csv',
        python_callable=download_usda_csv
    )
