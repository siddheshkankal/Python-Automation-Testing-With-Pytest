import pytest

def test_delItem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1


def test_removeItem(setup02):
    print(setup02)
    setup02.remove('wed')
    assert setup02 == pytest.weekdays2

    #
    # (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/py_fixtures/test_fixtures03.py --setup-show
    # ================================================= test session starts =================================================
    # platform win32 -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- D:\mine\Python Automation Testing With Pytest\Pytest-Automation\venv\Scripts\python.exe
    # cachedir: .pytest_cache
    # rootdir: D:\mine\Python Automation Testing With Pytest\Pytest-Automation
    # configfile: pytest.ini
    # collected 2 items
    #
    # Pytest_topics/py_fixtures/test_fixtures03.py::test_delItem
    #     SETUP    M setup01
    #         Pytest_topics/py_fixtures/test_fixtures03.py::test_delItem (fixtures used: setup01)PASSED
    # Pytest_topics/py_fixtures/test_fixtures03.py::test_removeItem
    #         SETUP    F setup02
    #         Pytest_topics/py_fixtures/test_fixtures03.py::test_removeItem (fixtures used: setup02)PASSED
    #         TEARDOWN F setup02
    #     TEARDOWN M setup01
    #
    # ================================================== 2 passed in 0.06s ==================================================
    #
    # (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  Pytest_topics/py_fixtures/test_fixtures03.py --setup-show
















# pytest -v  -k test_fixtures03.py --setup-show -s

