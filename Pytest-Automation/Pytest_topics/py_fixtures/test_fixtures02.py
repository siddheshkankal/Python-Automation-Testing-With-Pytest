import os

import pytest

weekdays1 = ['sun','mon','tue']
weekdays2 = ['thur','fri','sat']
filename = '../file1.txt'

#### tear down approach


@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('wed')
    yield wk1
    print('\n\n after yield in setup01 fixture')
    # wk1.pop()
    wk1.clear()


@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0,'wed')
    yield wk2



@pytest.fixture()
def setup03():
    f = open(filename,'w')
    f.write("Pytest is good")
    f.close()
    f = open(filename,'r+')
    yield f
    print("\n after the test is performed to clean the file")
    f.close()
    os.remove(filename)

def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['sun','mon','tue','wed','thur','fri','sat']

def test_len(setup01,setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)

# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/test_fixtures02.py -s

def test_filetest(setup03):
    assert (setup03.readline()) == 'Pytest is good'
#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/test_fixtures02.py -k "test_filetest" -s
# ================================================= test session starts =================================================
# platform win32 -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- D:\mine\Python Automation Testing With Pytest\Pytest-Automation\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: D:\mine\Python Automation Testing With Pytest\Pytest-Automation
# configfile: pytest.ini
# collected 3 items / 2 deselected / 1 selected
#
# Pytest_topics/test_fixtures02.py::test_filetest PASSED
#
# =========================================== 1 passed, 2 deselected in 0.03s ===========================================
#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/test_fixtures02.py -k "test_filetest" -s



