""" Provides a simple Python interface to the OSDU Storage API.
"""
from typing import List
import requests
import json
from .base import BaseService


class WorkflowService(BaseService):

    def __init__(self, client):
        super().__init__(client, service_name='workflow', service_version=1)

    def osdu_ingest(self, manifest):

        url = f'{self._service_url}/workflow/Osdu_ingest/workflowRun'
        
        payload = {
            "executionContext": {
                "Payload": {
                    "AppKey": "ts-osdu-script",
                    "data-partition-id": "osdu"
                },
                "manifest": manifest
            }
        }
        
        response = self.__execute_post_request(url, json=payload)
        response.raise_for_status()
        return response.json()

    def __execute_get_request(self, url: str, json: dict):
        headers = self._headers(json)
        response = requests.get(url=url, headers=headers, json=json)

        return response

    def __execute_post_request(self, url: str, json: dict):
        headers = self._headers(json)
        response = requests.post(url=url, headers=headers, json=json)
        #print(response.content)
        #response.raise_for_status()

        return response
