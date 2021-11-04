import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib3
import tfe_organization
import tfe_team
import tfe_team_access
import tfe_workspace
import tfe_workspace_variables

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Tfe(tfe_organization.TfeOrganization, tfe_team.TfeTeam, tfe_team_access.TfeTeamAccess, tfe_workspace.TfeWorkspace, tfe_workspace_variables.TfeVariables):
    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/vnd.api+json'

    def __init__(self, host, auth_token):
        self.host = host
        self.auth_token = auth_token
