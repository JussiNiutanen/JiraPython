'''
@author: Jussi Niutanen
Module create new issue to the ongoing sprint
'''
import sys

from as_auto_sprint import MyData
from it_issue_transition import MyLogin

mylogin = MyLogin()
mydata = MyData(MyData.URL,MyData.BOARD_ID,MyData.USER,"")
project_key = mydata.get_project_key()
sprint_id, name = mylogin.my_get_sprint()

try:
    sys.argv[1]
    name = sys.argv[1]
except IndexError:
    name = "New issue to" + name

mydata.create_issues(project_key,int(sprint_id),name)
