import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date
#import tfe_organization
from tfe_organization import TfeOrganization
#import tfe_workspace
from tfe_workspace import TfeWorkspace

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Tfe(TfeOrganization, TfeWorkspace):
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'

    def __init__(self, host):
        self.host = host
