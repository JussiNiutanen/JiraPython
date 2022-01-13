'''
@author: Jussi Niutanen
Content of common_test.py
'''

import os
import sys
from it_issue_transition import MyLogin
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("auto_sprint"), '..')))

TEST_STRING = '"endDate": "2022-01-14T05:33:05.000Z”,” id": 183, “name": "DDL Sprint 45", \
    "originBoardId": 28, "self": "https://niutanen.atlassian.net/rest/agile/1.0/sprint/183", \
    "startDate": "2022-01-07T05:33:05.000Z", "state": "future"'

def test_mylogin():
    """ Test for MyLogin class """

    with open('./config.yaml','r',encoding='utf8') as conf_file:
        data = yaml.load(conf_file, Loader=yaml.FullLoader)

    my = MyLogin(data)
    current_state = my.strip_and_casefold(sys.argv[1])
    new_state = my.strip_and_casefold(sys.argv[2])

    active_sprint_id, active_sprint_name = my.my_get_sprint()
    KEY = my.my_get_issue_key(active_sprint_id,current_state)
    my.progress_issue(KEY,new_state)

def get_sprint_id():
    '''Example for func test, return param + 1'''
    common = MyCommonFunc()
    common.get_sprint_details(TEST_STRING, 0)
    common.get_sprint_id()
