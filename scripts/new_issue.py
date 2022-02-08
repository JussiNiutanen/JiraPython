'''
@author: Jussi Niutanen
Module create new issue to the ongoing sprint
'''
import sys

from as_auto_sprint import MyData
from it_issue_transition import MyLogin

mylogin = MyLogin()

try:
    BOARD_ID = sys.argv[1]
except IndexError:
    BOARD_ID = MyData.BOARD_ID

mydata = MyData(MyData.URL,BOARD_ID,MyData.USER,"")
project_key = mydata.get_project_key()
sprint_id, name = mylogin.my_get_sprint()

try:
    name = sys.argv[2]
except IndexError:
    name = "New issue to " + name

mydata.create_issues(project_key,int(sprint_id),name)
