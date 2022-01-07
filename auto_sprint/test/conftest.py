'''
@author: Jussi Niutanen
Content of conftest.py
'''

def pytest_addoption(parser):
    """ pytest addoption for input parameter """
    parser.addoption("--stringinput", action="append", default=[],
        help="list of stringinputs to pass to test functions")

def pytest_generate_tests(metafunc):
    """ pytest generate test for input parameters """
    if 'stringinput' in metafunc.fixturenames:
        metafunc.parametrize("stringinput",
        metafunc.config.getoption('stringinput'))
