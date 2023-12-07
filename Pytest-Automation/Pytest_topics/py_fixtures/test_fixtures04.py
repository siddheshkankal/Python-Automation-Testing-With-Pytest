import pytest

# @pytest.fixture(params= [(3,4),[3,5]])
# def fixture01(request):
#     return request.param


@pytest.fixture(params= [(3,4),[3,5]],ids=['tuple','list'])
def fixture01(request):
    return request.param

def test_fix_param01(fixture01):
    assert (type(fixture01)) in  [tuple,list]



# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  -k test_fixtures04.py --setup-show -s



# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v  -k test_fixtures04.py -s

