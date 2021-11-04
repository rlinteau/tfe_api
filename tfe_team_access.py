import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TfeTeamAccess:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'
    
    def __init__(self, host):
        self.host = host
        self.auth_token = auth_token

    def add_access_to_workspace(self, workspace_id, team_id, access_perms):
        url = f"https://{self.host}/api/v2/team-workspaces"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
        payload = {
                    "data": {
                      "attributes": {
                        "access": access_perms,
                      },
                      "relationships": {
                        "workspace": {
                          "data": {
                            "type": "workspaces",
                            "id": workspace_id 
                          }
                        },
                      "team": {
                        "data": {
                          "type": "teams",
                          "id": team_id 
                        }
                      }
                    },
                    "type": "team-workspaces"
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
