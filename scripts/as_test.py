'''
@author: Jussi Niutanen
Content of as_main_test.py
'''

from as_auto_sprint import MyData

def test_valid_string():
    """ Sprint close and create test """

    mydata = MyData(MyData.URL, MyData.BOARD_ID, MyData.USER, "")
    assert mydata.update_sprints() == 200
