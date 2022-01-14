'''
@author: Jussi Niutanen
Module create new issue to the ongoing sprint
'''

from as_auto_sprint import MyData
from it_issue_transition import MyLogin

URL= "https://niutanen.atlassian.net/"
BOARD_ID = "29"
USER = "jussi.niutanen@gmail.com"

mylogin = MyLogin()
mydata = MyData(URL,BOARD_ID,USER,"")
project_key = mydata.get_project_key()
sprint_id, name = mylogin.my_get_sprint()
mydata.new_issue(project_key,int(sprint_id),name + "Issue name for new issue")
