import sys
import requests
import json
#from _dummy_thread import exit
#from datetime import datetime, timedelta
#import logging from _ast import If
import yaml

todo = 'todo';
progress = 'progress';
done = 'done';
today = 'today';
feedback = 'feedback';

class MyLogin:
    def __init__(self, config):
        self.c_jira_url = self.strip_and_casefold(config['url']);
        self.c_boar_id = config['board']; 
        self.c_user = self.strip_and_casefold(config['user']);
        self.c_apikey = (config['apikey']).strip();
        self.c_accept_header = {"Accept": "application/json"};
        self.todo = [todo,config[todo]];
        self.progress = [progress, config[progress]];
        self.done = [done,config[done]];
        self.today = [today,config[today]];
        self.feedback = [feedback,config[feedback]];        
#        logging.basicConfig(level=logging.DEBUG, 
#                            format='%(asctime)s %(levelname)s %(message)s', 
#                            filename='/tmp/auto_sprint.log', filemode='w')

    """ Debug log """
    def debug_log(self,log_text, log_id =""):
#        logging.debug(log_id);
#        logging.debug(log_text);
        print(log_text);
        print(log_id);
#        print(log_text);
#        logging.debug(json.dumps(json.loads(log_text), sort_keys=True, indent=4, separators=(",", ": ")))
#        print(log_id);
#        print(json.dumps(json.loads(response_new_sprint.text), sort_keys=True, indent=4, separators=(",", ": ")))

    def my_get_sprint(self):
        url = self.c_jira_url + "/rest/agile/1.0/board/" + str(self.c_boar_id) + "/sprint"
        #headers = {"Accept": "application/json"}
        # Get all sprints
        response_get = requests.get(url, headers=self.c_accept_header, auth=(self.c_user, self.c_apikey))
        # Save position of the active text to id parameter.
        res = response_get.text;
        self.debug_log(json.dumps(json.loads(res), sort_keys=True, indent=4, separators=(",", ": ")),response_get);
        
        # For some reason sometimes the request returns active sprint from other board. 
        # The next lines will filter sprints related to other boards away.
        input_dict = json.loads(res);
        output_dict = [x for x in input_dict['values'] if x['originBoardId'] == self.c_boar_id];

        res = ' '.join(map(str, output_dict));
        
        active_pos = res.find("active");
    
        id_postion = res.rfind("\'id\'", 0,active_pos);
        # Remove not needed marks from the begining of the string
        sprint_id = res[id_postion+5::]
        # Copy string for later to get the name
        sprint_name = sprint_id;
        # Remove not needed marks from the end of the sring
        sprint_id = sprint_id[0:sprint_id.find(",")];
    
        # Save position of the sprint name text to id parameter.
        name_position = sprint_name.find("\'name\'");
        # Remove not needed marks from the begining of the string
        sprint_name = sprint_name[name_position+9::]
        # Remove not needed marks from the end of the sring
        sprint_name = sprint_name[0:sprint_name.find("\'")];
       
        return sprint_id.strip(), sprint_name.strip();

    #my_find(res,"TODAY", "\"key\":\"");
    def my_find(self, input_text, tag1):
#        print(json.dumps(json.loads(input_text), sort_keys=True, indent=4, separators=(",", ": ")))

        tag1_pos = input_text.find(tag1);
    
        #tag2_postion = input_text.rfind(tag2, 0, tag1_pos);
        # Remove not needed marks from the begining of the string
        tag1_name = input_text[tag1_pos+7::]
        # Remove not needed marks from the end of the sring
        tag1_name = tag1_name[0:tag1_name.find("\'")];
        return tag1_name.strip();
        
    def my_get_issue_key(self, sprint_id,current_state):
        url = self.c_jira_url + "/rest/agile/1.0/sprint/" + sprint_id + "/issue"
        
        response_get = requests.get(url, headers=self.c_accept_header, auth=(self.c_user, self.c_apikey))

        res = response_get.text;
        print(res)
        #self.debug_log(json.dumps(json.loads(res), sort_keys=True, indent=4, separators=(",", ": ")),response_get);
        
        input_dict = json.loads(res);
#        print(input_dict);
#TOIMIVA
#        output_dict = [x for x in input_dict['issues'] if x['fields']['status']['name'] == 'TODAY'];

        output_dict = [x for x in input_dict['issues'] if self.strip_and_casefold(x['fields']['status']['name']) == current_state];

#        output_dict = [x for x in input_dict['issues'] if x['expand'] == "operations,versionedRepresentations,editmeta,changelog,renderedFields"];
#        output_dict = [x for x in input_dict['issues'] if x['fields']['timespent'] == 3900];
#        output_dict = [x for x in input_dict['issues'] if x['fields']['status']['id'] == '10073'];

        res = ' '.join(map(str, output_dict));
        print(res);
        res = res.replace(" ","");
        print(res)

        key_name = self.my_find(res,"\'key\':");
        return key_name;

    def get_transitoin_id(self,state):
        if(state == self.todo[0]):
            return self.todo[1];
        elif(state == self.progress[0]):
            return self.progress[1];
        elif(state == self.done[0]):
            return self.done[1];
        elif(state == self.today[0]):
            return self.today[1];
        elif(state == self.feedback[0]):
            return self.feedback[1];
        else:
            print("\n ERROR IN COLUMN NUMBER \n");
            exit();

    def progress_issue(self,key,result_state):
        
        url = self.c_jira_url + "/rest/api/2/issue/" + key + "/transitions";
        transition_id = self.get_transitoin_id(result_state);

        #transition_id = 21; #Progress
        #if(result_state=="done"):
        #    transition_id = 31; #Done
        payload = json.dumps({"update": {"comment": [{"add": {"body": "Comment added"}}]},"transition": {"id": str(transition_id)}})
        header = {"Content-Type": "application/json"};
        
        response_post = requests.post(url, data=payload, headers=header, auth=(self.c_user, self.c_apikey));
        print(response_post);

    def strip_and_casefold(self,text):
        text = text.strip().casefold();
        return text;