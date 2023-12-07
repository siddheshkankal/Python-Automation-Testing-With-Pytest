import sys
import pytest

# this will skip all the test cases skip entire file
# pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason = "run only on linux OS")



const = 9/5
def celcius_to_fah(cent = 0):
    fah = (cent * const) + 32
    return fah


# print(celcius_to_fah())

@pytest.mark.skip(reason = "Skipping for no reason specified")
def test_case1():
    assert type(const) == float

@pytest.mark.skipif(sys.version_info > (4,0), reason = "does not run on my version above 3.6")
def test_case2():
    assert celcius_to_fah() == 32.0


@pytest.mark.skipif(pytest.__version__ < '7.4.9' , reason = "pytest version less")
def test_case3():
    assert celcius_to_fah(38) == 100.4



# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -s Pytest_topics\test_skiptests.py::test_case2

# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -s Pytest_topics\test_skiptests.py::test_case2




