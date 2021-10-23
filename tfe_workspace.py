import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TfeWorkspace:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'

    def __init__(self, host):
        self.host = host

    def check_workspace_exist(self, auth_token, org_name, workspace_name):
        url = f"https://{self.host}/api/v2/organizations/{org_name}/workspaces/{workspace_name}"
        self.headers['Authorization'] = 'Bearer {}'.format(auth_token)

        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
        except Exception:
            pass
            
        if response.status_code == 200:
            return True
        else:
            return False
