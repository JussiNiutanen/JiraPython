# content of as_main_test.py

def func(param):
    '''Example for func test, return param + 1'''
    return param + 1

def test_answer():
    '''Example for func test'''
    assert func(4) == 5
