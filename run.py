import os
#import tfe
from tfe import Tfe
#from tfe_organization import TfeOrganization
#from tfe_workspace import TfeWorkspace

host = "app.terraform.io"

try:
    auth_token = os.environ['TFE_TOKEN']
    github_oauth_token = os.environ['GITHUB_OAUTH_TOKEN']
except KeyError:
    print("TFE_TOKEN or GITHUB_OAUTH_TOKEN missing!")
    sys.exit(1)

## Test if Org exist
xxx = Tfe(host)
test = xxx.check_organization_exist(auth_token, 'RLInfo')
print(test)

## Test if Workspace exist
xxx = Tfe(host)
test = xxx.check_workspace_exist(auth_token, 'RLInfo', 'test')
print(test)

## Test if Workspace exist
xxx = Tfe(host)
workspace_id = xxx.get_workspace_id(auth_token, 'RLInfo', 'abc123')
print(workspace_id)

## Test if Workspace exist
#xxx = Tfe(host)
#test = xxx.create_workspace_vcs(auth_token, 'RLInfo', 'abc123', '1.0.2', '/terraform', 'rlinteau/tfe_api', github_oauth_token)
#print(test)

# TFE var create
xxx = Tfe(host)
#test = xxx.create_variable_string(auth_token, 'ws-8f91WqLa1xV6ZYwT', 'var1', 'key1', False)
test = xxx.create_variable_string(auth_token, workspace_id, 'var1', 'key1', False)
print(test)
