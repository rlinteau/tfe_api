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
xxx = Tfe(host, auth_token)
test = xxx.check_organization_exist('RLInfo')
print(test)

## Test if Workspace exist
xxx = Tfe(host, auth_token)
test = xxx.check_workspace_exist('RLInfo', 'test')
print(test)

## Test if Workspace exist
xxx = Tfe(host, auth_token)
workspace_id = xxx.get_workspace_id('RLInfo', 'abc123')
print(workspace_id)

## Test if Workspace exist
#xxx = Tfe(host, auth_token)
#test = xxx.create_workspace_vcs('RLInfo', 'abc123', '1.0.2', '/terraform', 'rlinteau/tfe_api', github_oauth_token)
#print(test)

# TFE var create
#xxx = Tfe(host, auth_token)
#test = xxx.create_variable_string('ws-8f91WqLa1xV6ZYwT', 'var1', 'key1', False)
#test = xxx.create_variable_string(workspace_id, 'var1', 'key1', False)
print(test)

# TFE var found
xxx = Tfe(host, auth_token)
test = xxx.get_variable_id(workspace_id, 'var1')
print(f"Variable found: {test}")

# TFE var not found
xxx = Tfe(host, auth_token)
test = xxx.get_variable_id(workspace_id, 'notexist')
print(f"Variable not found: {test}")

# Update TFE
xxx = Tfe(host, auth_token)
test = xxx.update_variable_string('ws-8f91WqLa1xV6ZYwT', 'var-oaPMssmYQ9B8CKDr', 'var1',  'truite1', False)
print(f"Variable update: {test}")

# Update TFE
xxx = Tfe(host, auth_token)
test = xxx.update_variable_string('ws-8f91WqLa1xV6ZYwT', 'var-oaPMssmYQ9B8CKDrXXX', 'var1',  'truite1', False)
print(f"Variable update error: {test}")
