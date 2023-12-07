import pytest


@pytest.fixture()
def setup_list():
    print('\n in fixtures...\n')
    city = ['New York','London','Riyadh','Singapore','Mumbai']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York','Riyadh','Mumbai']


def reverse_list(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    print(setup_list[::-1])
    # assert setup_list[::-1] == ['Mumbai','Singapore','Riyadh','London','New York']
    assert setup_list[::-1] == reverse_list(setup_list)

#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -k "reverseList"
# ================================================= test session starts =================================================
# platform win32 -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- D:\mine\Python Automation Testing With Pytest\Pytest-Automation\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: D:\mine\Python Automation Testing With Pytest\Pytest-Automation
# configfile: pytest.ini
# collected 35 items / 34 deselected / 1 selected
#
# Pytest_topics/test_fixtures01.py::test_reverseList PASSED                                                        [100%]
#
# ========================================== 1 passed, 34 deselected in 0.05s ===========================================
#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -k "reverseList"


@pytest.mark.xfail(reason = "known issue: useFixtures can not use the fixtures return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixtruredemo():
    assert 1 == 1
    assert (setup_list[0])
    # print(setup_list[0])  #### it failes here
## with this kind of calling fixture we  cant use setup_list returning list


