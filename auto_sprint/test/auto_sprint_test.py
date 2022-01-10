'''
@author: Jussi Niutanen
Content of as_main_test.py
'''

import os
import sys
from auto_sprint import MyData
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("auto_sprint"), '..')))

def test_valid_string(): #stringinput):
    """ Sprint close and create test """

    # The APIKEY is store as environment variable is in .bash_profile in computer
    # and secret in GitHub workflow environmtent
    consumer_secret = os.environ.get('TESTKEY')
    assert len(consumer_secret) > 0

    url= "https://niutanen.atlassian.net/"
    board_id = "28"
    user = "jussi.niutanen@gmail.com"

    mydata = MyData(url, board_id, user, consumer_secret)
    assert mydata.update_sprints() == 200

def func(param):
    '''Example for func test, return param + 1'''
    return param + 1

def test_answer():
    '''Example for func test'''
    assert func(4) == 5
