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

    def create_variable_string(self, auth_token, workspace_id, var_key, var_value, var_sensitive):
        url = f"https://{self.host}/api/v2/vars"
        self.headers['Authorization'] = 'Bearer {}'.format(auth_token)
        payload = {
                    "data": {
                      "type":"vars",
                      "attributes": {
                        "key":var_key,
                        "value":var_value,
                        "category":"terraform",
                        "hcl":"false",
                        "sensitive":var_sensitive
                       },
                      "relationships": {
                        "workspace": {
                          "data": {
                            "id":workspace_id,
                            "type":"workspaces"
                          }
                        }
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
