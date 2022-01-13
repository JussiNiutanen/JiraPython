'''
@author: Jussi Niutanen
Content of common_test.py
'''

import yaml
import os
from it_issue_transition import MyLogin

CURRENT = "TO DO"
NEW = "DONE"

TEST_STRING = '"endDate": "2022-01-14T05:33:05.000Z”,” id": 183, “name": "DDL Sprint 45", \
    "originBoardId": 28, "self": "https://niutanen.atlassian.net/rest/agile/1.0/sprint/183", \
    "startDate": "2022-01-07T05:33:05.000Z", "state": "future"'

def test_mylogin():
    """ Test for MyLogin class """

    with open('./it_config.yaml','r',encoding='utf8') as conf_file:
        data = yaml.load(conf_file, Loader=yaml.FullLoader)

    mylogin = MyLogin(data)

    # The APIKEY is store as environment variable is in .bash_profile in computer
    # and secret in GitHub workflow environmtent
    mylogin.set_apikey(os.environ.get('TESTKEY'))

    current_state = mylogin.strip_and_casefold(CURRENT)
    new_state = mylogin.strip_and_casefold(NEW)

    active_sprint_id, active_sprint_name = mylogin.my_get_sprint()
    KEY = mylogin.my_get_issue_key(active_sprint_id,current_state)
#    mylogin.progress_issue(KEY,new_state)
