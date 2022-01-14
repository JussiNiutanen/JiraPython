'''
@author: Jussi Niutanen
Content of as_main_test.py
'''

import os
#import sys
from as_auto_sprint import MyData
from it_issue_transition import MyLogin

url= "https://niutanen.atlassian.net/"
board_id = "29"
user = "jussi.niutanen@gmail.com"

def test_valid_string(): #stringinput):
#    """ Sprint close and create test """

    mydata = MyData(url, board_id, user, "")
    assert mydata.update_sprints() == 200

def test_create_issue():
#    """ Test create issue"""
    mydata = MyData(url, board_id, user, "")
    mylogin = MyLogin()

    mydata = MyData(url,board_id,user,"")
    project_key = mydata.get_project_key()
    sprint_id, name = mylogin.my_get_sprint()
    name
    mydata.new_issue(project_key,int(sprint_id),"Issue name for new issue")
