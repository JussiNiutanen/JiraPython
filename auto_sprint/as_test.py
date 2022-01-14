'''
@author: Jussi Niutanen
Content of as_main_test.py
'''

from as_auto_sprint import MyData
from it_issue_transition import MyLogin

URL= "https://niutanen.atlassian.net/"
BOARD_ID = "29"
USER = "jussi.niutanen@gmail.com"

def test_valid_string():
    """ Sprint close and create test """

    mydata = MyData(URL, BOARD_ID, USER, "")
    assert mydata.update_sprints() == 200

def test_create_issue():
    """ Test create issue"""
    mylogin = MyLogin()
    mydata = MyData(URL,BOARD_ID,USER,"")
    project_key = mydata.get_project_key()
    sprint_id, name = mylogin.my_get_sprint()
    mydata.new_issue(project_key,int(sprint_id),name + "Issue name for new issue")
