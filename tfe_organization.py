import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TfeOrganization:
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'
    
    def __init__(self, host, auth_token):
        self.host = host
        self.auth_token = auth_token

    def check_organization_exist(self, org_name):
        url = f"https://{self.host}/api/v2/organizations/{org_name}"
        self.headers['Authorization'] = 'Bearer {}'.format(self.auth_token)

        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                return True
        except requests.exceptions.HTTPError as err:
            print(err)
 
        return False
