
import pytest
pytestmark = [pytest.mark.smoke]

@pytest.mark.sanity
def test_a1():
    print('first test case')
    assert  5 + 5 == 10

@pytest.mark.sanity_latest
def test_a2():
    assert  9/5 == 1.8,"failed test"

@pytest.mark.sanity_latest
@pytest.mark.sanity
def test_a3():
    assert  9//5 == 1,"failed test a3"







# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m sanity Pytest_topics\test_markers.py


# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m "sanity and not sanity_latest" Pytest_topics\test_markers.py

# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m "not sanity" Pytest_topics\test_markers.py


# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m "sanity and  sanity_latest" Pytest_topics\test_markers.py

# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m "sanity or sanity_latest" Pytest_topics\test_markers.py

# no need to mention file path
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -m smoke

# to get rid of warnings create a pytest.ini file in root directory and define the marks

