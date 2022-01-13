'''
@author: Jussi Niutanen
Issue transition main module
'''

import sys
import os
from it_issue_transition import MyLogin

try:
    sys.argv[1], sys.argv[2]
except IndexError:
    print("\n TOO FEW PARAMETERS \n")
    sys.exit()

#CONFIG_PATH = "./auto_sprint/it_config.yaml"

#with open(CONFIG_PATH,'r',encoding='utf8') as conf_file:
#    data = yaml.load(conf_file, Loader=yaml.FullLoader)

#mylogin = MyLogin(data)
mylogin = MyLogin()

# The APIKEY is store as environment variable is in .bash_profile in computer
# and secret in GitHub workflow environmtent
mylogin.set_apikey(os.environ.get('TESTKEY'))

current_state = mylogin.strip_and_casefold(sys.argv[1])
new_state = mylogin.strip_and_casefold(sys.argv[2])

active_sprint_id, active_sprint_name = mylogin.my_get_sprint()
KEY = mylogin.my_get_issue_key(active_sprint_id,current_state)
mylogin.progress_issue(KEY,new_state)
