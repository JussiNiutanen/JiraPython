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
