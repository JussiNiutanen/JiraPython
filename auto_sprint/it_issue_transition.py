'''
@author: Jussi Niutanen
Issue transition module
'''

import json
import os
import sys
from pathlib import Path
import requests
import yaml

# The transition id might depend on the board with id 20
TODO = 'todo'
PROGRESS = 'progress' #transition_id = 21 in the board with id 20
DONE = 'done' #transition_id = 31 in the board with id 20
TODAY = 'today'
FEEDBACK = 'feedback'

CONFIG_PATH = os.path.join(Path.home(), "it_config.yaml")

class MyLogin:
    """ MyLogin class """

    def __init__(self):
        with open(CONFIG_PATH,'r',encoding='utf8') as conf_file:
            config = yaml.safe_load(conf_file)
            #config = yaml.safe_load(conf_file, Loader=yaml.FullLoader)

        self.c_jira_url = self.strip_and_casefold(str(config['url']))
        self.c_boar_id = config['board']
        self.c_user = self.strip_and_casefold(str(config['user']))
        self.c_accept_header = {"Accept": "application/json"}
        self.config = config

        # The APIKEY is store as environment variable is in .bash_profile in computer
        # and secret in GitHub workflow environmtent
        env_apikey = os.environ.get('TESTKEY')
        self.c_apikey = env_apikey

        #yaml_apikey = str(config['apikey']).strip()
        #if yaml_apikey != "None":
        #    self.c_apikey = yaml_apikey

#        logging.basicConfig(level=logging.DEBUG,
#                            format='%(asctime)s %(levelname)s %(message)s',
#                            filename='/tmp/auto_sprint.log', filemode='w')

    def set_apikey(self,apikey):
        """ Set apikey internal variable """
        self.c_apikey = apikey

    @staticmethod
    def debug_log(log_text, log_id =""):
        """ Debug log """
#        logging.debug(log_id)
#        logging.debug(log_text)
        print(log_text)
        print(log_id)
#        print(log_text)
#        logging.debug(json.dumps(json.loads(log_text), sort_keys=True,
#           indent=4, separators=(",", ": ")))
#        print(log_id)
#        print(json.dumps(json.loads(response_new_sprint.text), sort_keys=True,
#           indent=4, separators=(",", ": ")))

    def my_get_sprint(self):
        """ my_get returns sprint id """
        url = self.c_jira_url + "/rest/agile/1.0/board/" + str(self.c_boar_id) + "/sprint"
        #headers = {"Accept": "application/json"}
        # Get all sprints
        response_get = requests.get(url, headers=self.c_accept_header,
            auth=(self.c_user, self.c_apikey))
        # Save position of the active text to id parameter.
        res = response_get.text
        self.debug_log(json.dumps(json.loads(res), sort_keys=True, indent=4,
            separators=(",", ": ")),response_get)

        # For some reason sometimes the request returns active sprint from other board.
        # The next lines will filter sprints related to other boards away.
        input_dict = json.loads(res)
        output_dict = [x for x in input_dict['values'] if x['originBoardId'] == self.c_boar_id]

        res = ' '.join(map(str, output_dict))

        active_pos = res.find("active")

        id_postion = res.rfind("\'id\'", 0,active_pos)
        # Remove not needed marks from the begining of the string
        sprint_id = res[id_postion+5::]
        # Copy string for later to get the name
        sprint_name = sprint_id
        # Remove not needed marks from the end of the sring
        sprint_id = sprint_id[0:sprint_id.find(",")]

        # Save position of the sprint name text to id parameter.
        name_position = sprint_name.find("\'name\'")
        # Remove not needed marks from the begining of the string
        sprint_name = sprint_name[name_position+9::]
        # Remove not needed marks from the end of the sring
        sprint_name = sprint_name[0:sprint_name.find("\'")]

        return sprint_id.strip(), sprint_name.strip()

    @staticmethod
    def my_find(input_text, tag1):
        """ my_find finds tag1 from input text """
        tag1_pos = input_text.find(tag1)

        #tag2_postion = input_text.rfind(tag2, 0, tag1_pos)
        # Remove not needed marks from the begining of the string
        tag1_name = input_text[tag1_pos+7::]
        # Remove not needed marks from the end of the sring
        tag1_name = tag1_name[0:tag1_name.find("\'")]
        return tag1_name.strip()

    def my_get_issue_key(self, sprint_id,current_state):
        """ my_get returns issue key """
        url = self.c_jira_url + "/rest/agile/1.0/sprint/" + sprint_id + "/issue"

        response_get = requests.get(url, headers=self.c_accept_header,
            auth=(self.c_user, self.c_apikey))

        res = response_get.text
        print(res)

        input_dict = json.loads(res)

        output_dict = [x for x in input_dict['issues']
            if self.strip_and_casefold(x['fields']['status']['name']) == current_state]

        res = ' '.join(map(str, output_dict))
        print(res)
        res = res.replace(" ","")
        print(res)

        key_name = self.my_find(res,"\'key\':")
        return key_name

    def get_transitoin_id(self,state):
        """ Returns transition id """
        transition_id = 0

        # Get transition id from the yaml file and add it to parameter
        if state == TODO :
            transition_id = self.config[TODO]
        elif state == PROGRESS :
            transition_id = self.config[PROGRESS]
        elif state == DONE :
            transition_id = self.config[DONE]
        elif state == TODAY :
            transition_id = self.config[TODAY]
        elif state == FEEDBACK :
            transition_id = self.config[FEEDBACK]
        else:
            print("\n ERROR IN COLUMN NUMBER \n")
            sys.exit()

        return transition_id

    def progress_issue(self,key,result_state):
        """ Move issue (defined with the key) to new state """

        url = self.c_jira_url + "/rest/api/2/issue/" + key + "/transitions"
        transition_id = self.get_transitoin_id(result_state)

        payload = json.dumps({"update": {"comment": [{"add": {"body": "Comment added"}}]},
            "transition": {"id": str(transition_id)}})
        header = {"Content-Type": "application/json"}

        response_post = requests.post(url, data=payload, headers=header,
            auth=(self.c_user, self.c_apikey))
        print(response_post)

    @staticmethod
    def strip_and_casefold(text):
        """ Remove spaces and return the given text as lower case """
        text = text.strip().casefold()
        return text

    #class MyCreateIssue:
    #""" Class for adding issue to ongoing sprint """

#    @staticmethod
    def create_issue(self):
        """ Create issue """
        url = "https://niutanen.atlassian.net/rest/api/2/issue/"

        headers = {
        "Content-Type": "application/json"
        }

        payload = json.dumps( {
            "fields": {
                "project": {"key": "TE"},
                "summary": "REST ye merry gentlemen.",
                "issuetype": {
                  "name": "Story"
                }
            }
        } )

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=(self.c_user, self.c_apikey)
        )

        print(response.text)
