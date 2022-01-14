'''
@author: Jussi Niutanen
Issue transition main module
'''

import sys
from it_issue_transition import MyLogin
from as_auto_sprint import MyData

try:
    sys.argv[1], sys.argv[2]
except IndexError:
    print("\n TOO FEW PARAMETERS \n")
    sys.exit()

#mycreateissue = MyCreateIssue()
#mycreateissue.create_issue()

mylogin = MyLogin()

#current_state = mylogin.strip_and_casefold(sys.argv[1])
#new_state = mylogin.strip_and_casefold(sys.argv[2])

#active_sprint_id, active_sprint_name = mylogin.my_get_sprint()
#KEY = mylogin.my_get_issue_key(active_sprint_id,current_state)
#mylogin.progress_issue(KEY,new_state)

url= "https://niutanen.atlassian.net/"
board_id = "29"
user = "jussi.niutanen@gmail.com"
mydata = MyData(url,board_id,user,"")
project_key = mydata.get_project_key()
sprint_id, name = mylogin.my_get_sprint()
name
mydata.new_issue(project_key,int(sprint_id),"Issue name for new issue")
