'''
@author: Jussi Niutanen
Issue transition main module
'''

import sys
#import requests
#import json
#from _dummy_thread import exit
#from datetime import datetime, timedelta
#import logging from _ast import If

import yaml

from issue_transition import MyLogin
#import issu_transition import MyLogin

try:
    sys.argv[1], sys.argv[2]
except IndexError:
    print("\n TOO FEW PARAMETERS \n")
    sys.exit()

with open('./config.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)

my = MyLogin(data)
current_state = my.strip_and_casefold(sys.argv[1])
new_state = my.strip_and_casefold(sys.argv[2])

active_sprint_id, active_sprint_name = my.my_get_sprint()
KEY = my.my_get_issue_key(active_sprint_id,current_state)
my.progress_issue(KEY,new_state)
