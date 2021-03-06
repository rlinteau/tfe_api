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
        self.auth_token = auth_token

    def check_workspace_exist(self, org_name, workspace_name):
        url = f"https://{self.host}/api/v2/organizations/{org_name}/workspaces/{workspace_name}"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)

        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                return True
        except requests.exceptions.HTTPError as err:
            print(err)
            
        return False

    def get_workspace_id(self, org_name, workspace_name):
        url = f"https://{self.host}/api/v2/organizations/{org_name}/workspaces/{workspace_name}"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)

        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()["data"]["id"]
        except requests.exceptions.HTTPError as err:
            print(err)

        return False

    def create_workspace_vcs(self, org_name, workspace_name, tf_version, working_dir, vcs_repo_name, vcs_repo_oauth):
        url = f"https://{self.host}/api/v2/organizations/{org_name}/workspaces"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
        payload = {
                    "data": {
                      "attributes": {
                        "name": workspace_name,
                        "terraform_version": tf_version,
                        "working-directory": working_dir,
                        "vcs-repo": {
                          "identifier": vcs_repo_name,
                          "oauth-token-id": vcs_repo_oauth
                        },
                      },
                      "type": "workspaces"
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
