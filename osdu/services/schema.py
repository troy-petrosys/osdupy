""" Provides a simple Python interface to the OSDU Storage API.
"""
from typing import List
import requests
import json
from .base import BaseService


class SchemaService(BaseService):

    def __init__(self, client):
        super().__init__(client, service_name='schema-service', service_version=1)

    def get_schema(self, schema_id: str):
        """Returns the latest version of the given record."""
        url = f'{self._service_url}/schema/{schema_id}'
        response = self.__execute_get_request(url)

        return response.json()

    def get_all_schemas(self):
        """Returns the latest version of the given record."""
        url = f'{self._service_url}/schema'

        payload = {'limit': 1000, 'offset': 0, 'latestVersion': True}
        
        response = self.__execute_get_request(url, json=payload)

        return response.json()

    def add_schema(self, schema_file):
        """Returns the latest version of the given record."""
        url = f'{self._service_url}/schema'
        
        schema = ''
        with open(schema_file) as f:
#            schema = f.read()
            schema = json.loads(f.read())
       
        response = self.__execute_post_request(url, json=schema)

        return response.json()

    def __execute_get_request(self, url: str, json: dict):
        headers = self._headers(json)
        response = requests.get(url=url, headers=headers, json=json)

        return response

    def __execute_post_request(self, url: str, json: dict):
        headers = self._headers(json)
        response = requests.post(url=url, headers=headers, json=json)
        print(response.content)
        #response.raise_for_status()

        return response
