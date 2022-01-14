'''
@author: Jussi Niutanen
Sprint close and new sprint automation module
'''

import json
import os
from datetime import datetime, timedelta
import requests
from common.common import MyCommonFunc


class MyData:
    """ MyData class """
    URL= "https://niutanen.atlassian.net/"
    BOARD_ID = "29"
    USER = "jussi.niutanen@gmail.com"

    def __init__(self, instance_url, board_id, user, apikey):
        self.c_jira_url = instance_url
        self.c_boar_id = board_id
        self.c_user = user

        # The APIKEY is store as environment variable is in .bash_profile in computer
        # and secret in GitHub workflow environmtent
        env_apikey = os.environ.get('TESTKEY')
        self.c_apikey = env_apikey
        if len(str(apikey)) > 0:
            self.c_apikey = apikey

#        logging.basicConfig(level=logging.DEBUG,
#                            format='%(asctime)s %(levelname)s %(message)s',
#                            filename='/tmp/auto_sprint.log', filemode='w')
        self.c_accept_header = {"Accept": "application/json"}
        self.c_common_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    @staticmethod
    def debug_log(log_text, log_id =""):
        """ Debug log """
#        logging.debug(log_id);
#        logging.debug(log_text);
        print(log_id)
        print(log_text)
#        logging.debug(json.dumps(json.loads(log_text), sort_keys=True,
#        indent=4, separators=(",", ": ")))
#        print(log_id);
#        print(json.dumps(json.loads(response_new_sprint.text), sort_keys=True,
# indent=4, separators=(",", ": ")))

    def get_sprint(self, sprint_state):
        """ Returns spring id for the active spring in the board 3 """
        url = self.c_jira_url + "/rest/agile/1.0/board/" + self.c_boar_id + "/sprint"
        #headers = {"Accept": "application/json"}
        # Get all sprints
#        response_get = requests.get(url, headers=self.c_accept_header,
#                                    auth=(self.c_user, self.c_apikey))
        # Save position of the active text to id parameter.
 #       res = response_get.text
 #       self.debug_log(json.dumps(json.loads(res), sort_keys=True, indent=4,
 #                                   separators=(",", ": ")),response_get)

        # For some reason sometimes the request returns active sprint from other board.
        # The next lines will filter sprints related to other boards away.
#        input_dict = json.loads(res)

        common_data = MyCommonFunc()
        input_dict = common_data.make_request(requests,url,self.c_accept_header,
            self.c_user,self.c_apikey)
        output_dict = [x for x in input_dict['values'] if x['originBoardId'] == int(self.c_boar_id)]

        res = ' '.join(map(str, output_dict))

        active_pos = res.find(sprint_state)

        common_data.get_sprint_details(res, active_pos)
        #id_postion = common_data.get_id_position(common_data)
        sprint_id = common_data.get_sprint_id()
        sprint_name = common_data.get_sprint_name()
        #name_position = common_data.get_name_position(common_data)

        return sprint_id.strip(), sprint_name.strip()

    def close_sprint(self, sprint_id):
        """ Close active sprint """
        current_time_and_day = datetime.now().astimezone().replace(microsecond=0).isoformat()
        url_close = self.c_jira_url + "/rest/agile/1.0/sprint/" + sprint_id
        payload = json.dumps({
            "id": sprint_id,
            "self": url_close,
            "state": "closed",
            "completeDate": current_time_and_day
        })
        response_close = requests.post(url_close, data=payload, headers=self.c_common_headers,
            auth=(self.c_user, self.c_apikey))
        self.debug_log(json.dumps(json.loads(response_close.text), sort_keys=True,
            indent=4, separators=(",", ": ")),response_close)

    def create_sprint(self, old_sprint_name):
        """ Create new sprint """
        current_time_and_day = datetime.now().astimezone().replace(microsecond=0)
        end_time = current_time_and_day+ timedelta(days=7)
        url_new_sprint = self.c_jira_url + "/rest/agile/1.0/sprint/"
        name_len = len(old_sprint_name)
        last_space = old_sprint_name.rfind(" ",0,name_len)
        new_sprint_number = int(old_sprint_name[last_space:name_len].strip()) + 1
        new_sprint_name = old_sprint_name[0:last_space] + " " + str(new_sprint_number)
        print(new_sprint_name)

        payload_new_sprint = json.dumps( {
          "name": new_sprint_name,
          "startDate":current_time_and_day.isoformat(),
          "endDate":end_time.isoformat(),
          "originBoardId": self.c_boar_id
        } )

        response_new_sprint = requests.post(
           url_new_sprint,
           data=payload_new_sprint,
           headers=self.c_common_headers,
           auth=(self.c_user, self.c_apikey)
        )
        self.debug_log(json.dumps(json.loads(response_new_sprint.text), sort_keys=True,
            indent=4, separators=(",", ": ")),response_new_sprint)
        return new_sprint_name,new_sprint_number

    def get_project_key(self):
        """ Get project key (typically two letters) for the given board """
        url = self.c_jira_url + "/rest/agile/1.0/board/" + self.c_boar_id
        headers = {"Accept": "application/json"}

        response = requests.get(
           url,
           headers=headers,
           auth=(self.c_user, self.c_apikey)
        )

        res = response.text
        print(res)

        # Save position of the sprint name text to id parameter.
        key_position = res.find("\"projectKey\"") # length of projectKey 10
        # Remove not needed marks from the begining of the string
        key_name = res[key_position+14::]
        # Remove not needed marks from the end of the sring
        key_name = key_name[0:key_name.find("\"")]
        return key_name

    def new_issue(self, project_key,sprint_id,issue_summary):
        """ Create new story to the new sprint """
        payload_new_issue = json.dumps( {
            "fields": {
                "project":{"key": project_key},
                "summary": issue_summary,
                "issuetype": {"name": "Story"},
                "customfield_10021": sprint_id
           }
        })
        url_new_issue = self.c_jira_url + "/rest/api/2/issue/"
        my_headers = {"Content-Type": "application/json"}
        response_new_issue = requests.post(
           url_new_issue,
           data=payload_new_issue,
           headers=my_headers,
           auth=(self.c_user, self.c_apikey)
        )

        self.debug_log(json.dumps(json.loads(response_new_issue.text), sort_keys=True,
            indent=4, separators=(",", ": ")),response_new_issue)

    def start_sprint(self,sprint_id):
        """ Start sprint """
        payload_new_issue = json.dumps( {
                "id": sprint_id,
                "state": "active"
           })
        start_sprint = self.c_jira_url + "/rest/agile/1.0/sprint/" + str(sprint_id)
        response_new_sprint = requests.post(
           start_sprint,
           data=payload_new_issue,
           headers=self.c_common_headers,
           auth=(self.c_user, self.c_apikey)
        )

        self.debug_log(json.dumps(json.loads(response_new_sprint.text), sort_keys=True,
            indent=4, separators=(",", ": ")),response_new_sprint)

    def update_sprints(self):
        """ Update sprint """
        active_sprint_id, active_sprint_name  = self.get_sprint("active")
        self.close_sprint(active_sprint_id)

        self.create_sprint(active_sprint_name)
        future_sprint_id, future_sprint_name  = self.get_sprint("future")

        project_key = self.get_project_key()
        self.new_issue(project_key,int(future_sprint_id),"Planning " + future_sprint_name)
        self.start_sprint(int(future_sprint_id))

        return 200
