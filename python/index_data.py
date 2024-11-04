import requests
import csv
import os

SOLR_URL = 'http://localhost:8989/solr'
collection_name = 'Hash_Jayar'

def create_collection(collection_name):
    response = requests.get(f'{SOLR_URL}/admin/collections?action=CREATE&name={collection_name}')
    return response.json()

def index_data(collection_name, exclude_column):
    if not os.path.isfile('employee_data.csv'):
        print("Employee data file not found.")
        return
    
    try:
        with open('employee_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if exclude_column in row:
                    del row[exclude_column]
                response = requests.post(f'{SOLR_URL}/{collection_name}/update/json/docs', json=row)
                print(f'Indexing Response: {response.json()}')
    except UnicodeDecodeError:
        with open('employee_data.csv', 'r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if exclude_column in row:
                    del row[exclude_column]
                response = requests.post(f'{SOLR_URL}/{collection_name}/update/json/docs', json=row)
                print(f'Indexing Response: {response
