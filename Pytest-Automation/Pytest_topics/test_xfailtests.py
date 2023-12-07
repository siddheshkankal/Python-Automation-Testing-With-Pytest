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


# @pytest.mark.xfail(reason = "known issue")
# def test_a4():
#     letters = 'abcd'
#     assert letters[10]
#
@pytest.mark.xfail(raises=IndexError,reason = "known issue") # if we make raises = TypeError then tests will become fail
def test_a4():
    letters = 'abcd'
    assert letters[10]





@pytest.mark.xfail
def test_a5():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'


# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v Pytest_topics\test_xfailtests.py

#
# Pytest_topics/test_xfailtests.py::test_case1 SKIPPED (Skipping for no reason specified)                                             [ 20%]
# Pytest_topics/test_xfailtests.py::test_case2 PASSED                                                                                 [ 40%]
# Pytest_topics/test_xfailtests.py::test_case3 SKIPPED (pytest version less)                                                          [ 60%]
# Pytest_topics/test_xfailtests.py::test_a4 XPASS                                                                                     [ 80%]
# Pytest_topics/test_xfailtests.py::test_a5 XFAIL                                                                                     [100%]
#
# =========================================== 1 passed, 2 skipped, 1 xfailed, 1 xpassed in 0.17s ===========================================
#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>\



#
# Pytest_topics/test_xfailtests.py::test_case1 SKIPPED (Skipping for no reason specified)                                             [ 20%]
# Pytest_topics/test_xfailtests.py::test_case2 PASSED                                                                                 [ 40%]
# Pytest_topics/test_xfailtests.py::test_case3 SKIPPED (pytest version less)                                                          [ 60%]
# Pytest_topics/test_xfailtests.py::test_a4 XFAIL (known issue)                                                                       [ 80%]
# Pytest_topics/test_xfailtests.py::test_a5 XFAIL                                                                                     [100%]
#
# ================================================ 1 passed, 2 skipped, 2 xfailed in 0.19s =================================================
#
# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v Pytest_topics\test_xfailtests.py