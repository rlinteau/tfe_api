import os
from tfe_organization import TfeOrganization

host = "app.terraform.io"

try:
    auth_token = os.environ['TFE_TOKEN']
except KeyError:
    print("TFE_TOKEN missing!")
    sys.exit(1)

xxx = TfeOrganization(host)


test = xxx.check_organization_exist(auth_token, 'RLInfoa')

print(test)

