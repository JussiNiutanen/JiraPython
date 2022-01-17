'''
@author: Jussi Niutanen
Content of common_test.py
'''

from it_issue_transition import MyLogin

CURRENT = 'to do'
NEW = 'done'

#TEST_STRING = '"endDate": "2022-01-14T05:33:05.000Z”,” id": 183, “name": "DDL Sprint 45", \
#    "originBoardId": 28, "self": "https://niutanen.atlassian.net/rest/agile/1.0/sprint/183", \
#    "startDate": "2022-01-07T05:33:05.000Z", "state": "future"'

def test_mylogin():
    """ Test for MyLogin class """

    mylogin = MyLogin()

    current_state = mylogin.strip_and_casefold(CURRENT)
    new_state = mylogin.strip_and_casefold(NEW)

    active_sprint_id, active_sprint_name = mylogin.my_get_sprint()

    assert len(active_sprint_name) > 0

    issue_id = mylogin.my_get_issue_key(active_sprint_id,current_state)
    mylogin.progress_issue(issue_id,new_state)
