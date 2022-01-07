'''
@author: Jussi Niutanen
Content of as_main_test.py
'''

from ..auto_sprint.auto_sprints import MyData

def test_valid_string(stringinput):
    url= "https://niutanen.atlassian.net/"
#    id = 28
    user = "jussi.niutanen@gmail.com"
    key = "JIILK5GhdhOzSCOtQeXsC2CD"

    d = MyData(url, stringinput, user, key)
    assert d.update_sprints() == 0

def func(param):
    '''Example for func test, return param + 1'''
    return param + 1

def test_answer():
    '''Example for func test'''
    assert func(4) == 5

def test_one():
    '''Example for func test'''
    assert 1 == 1

def test_two():
    '''Example for func test'''
    assert 2 == 2
