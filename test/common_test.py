'''
@author: Jussi Niutanen
Content of common_test.py
'''

import os
import sys
from common._common import MyCommonFunc
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("as_auto_sprint"), '..')))

TEST_STRING = '"endDate": "2022-01-14T05:33:05.000Z”,” id": 183, “name": "DDL Sprint 45", \
    "originBoardId": 28, "self": "https://niutanen.atlassian.net/rest/agile/1.0/sprint/183", \
    "startDate": "2022-01-07T05:33:05.000Z", "state": "future"'

def test_common_get_sprint_details():
    """ Test for MyCommonFunc class """

    common = MyCommonFunc()
    common.get_sprint_details(TEST_STRING, 0)
    common.get_sprint_name()
    common.get_name_position()

def get_sprint_id():
    '''Example for func test, return param + 1'''
    common = MyCommonFunc()
    common.get_sprint_details(TEST_STRING, 0)
    common.get_sprint_id()
