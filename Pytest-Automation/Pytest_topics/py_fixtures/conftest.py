import pytest

def pytest_configure():
    pytest.weekdays1 = ['sun','mon','tue']
    pytest.weekdays2 = ['thur','fri','sat']

@pytest.fixture(scope = "module")
def setup01():
    wk1 = pytest.weekdays1.copy()
    wk1.append('wed')
    yield wk1
    print('\n\n  setup01 fixture closing')
    # pytest.weekdays1.pop()
    # wk1.clear()


@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0,'wed')
    yield wk2



# ================================================
# platform win32 -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- D:\mine\Python Automation Testing With Pytest\Pytest-Automation\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: D:\mine\Python Automation Testing With Pytest\Pytest-Automation
# configfile: pytest.ini
# collected 2 items
#
# Pytest_topics/py_fixtures/test_fixtures03.py::test_delItem ['sun', 'mon', 'tue']
# PASSED
# Pytest_topics/py_fixtures/test_fixtures03.py::test_removeItem ['wed', 'thur', 'fri', 'sat']
# PASSED
#
#  after yield in setup01 fixture
#
#
# ================================================== 2 passed in 0.06s ==================================================
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/py_fixtures/test_fixtures03.py -s




