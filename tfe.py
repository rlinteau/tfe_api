import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import time
from datetime import date
import tfe_organization
import tfe_workspace
import tfe_variables

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Tfe(tfe_organization.TfeOrganization, tfe_workspace.TfeWorkspace, tfe_variables.TfeVariables):
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'

    def __init__(self, host):
        self.host = host
