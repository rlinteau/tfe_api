import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TfeTeam:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'
    
    def __init__(self, host):
        self.host = host
        self.auth_token = auth_token

    def get_team_id(self, org_name, team_name):
        url = f"https://{self.host}/api/v2/organizations/{org_name}/teams?page%5Bsize%5D=50"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
             
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                content = response.json()
                for item in content['data']:
                    if item['attributes'].get('name') == team_name:
                        return item['id']
        except requests.exceptions.HTTPError as err:
            print(err)

        return False
