import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TfeVariables:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'
    
    def __init__(self, host):
        self.host = host
        self.auth_token = auth_token

    def create_variable_string(self, workspace_id, var_key, var_value, var_sensitive):
        url = f"https://{self.host}/api/v2/workspaces/{workspace_id}/vars"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
        payload = {
                    "data": {
                      "type":"vars",
                      "attributes": {
                        "key":var_key,
                        "value":var_value,
                        "category":"terraform",
                        "hcl":"false",
                        "sensitive":var_sensitive
                      }
                    }
                  }

        try:
            response = requests.post(url, headers=self.headers, json=payload, verify=False)
            response.raise_for_status()
            if response.status_code == 201:
                return True
        except requests.exceptions.HTTPError as err:
            print(err)

        return False

    def get_variable_id(self, workspace_id, var_key):
        url = f"https://{self.host}/api/v2/workspaces/{workspace_id}/vars"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)

        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()

            if response.status_code == 200:
                varlist = response.json()
                for item in varlist['data']:
                    if item['attributes']['key'] == var_key:
                        return item['id']
        except requests.exceptions.HTTPError as err:
            print(err)

        return False

    def update_variable_string(self, workspace_id, var_id, var_key, var_value, var_sensitive):
        url = f"https://{self.host}/api/v2/workspaces/{workspace_id}/vars/{var_id}"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
        payload = {
                    "data": {
                      "id":var_id,
                      "attributes": {
                        "key":var_key,
                        "value":var_value,
                        "category":"terraform",
                        "hcl": "false",
                        "sensitive": var_sensitive
                      },
                      "type":"vars"
                    }
                  }

        try:
            response = requests.patch(url, headers=self.headers, json=payload, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                return True
        except requests.exceptions.HTTPError as err:
            print(err)

        return False

