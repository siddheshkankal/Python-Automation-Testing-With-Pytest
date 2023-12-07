import pytest

def test_case1():
    # with pytest.raises(Exception):
    with pytest.raises(ZeroDivisionError):
        assert (1/0) # without upper line we will get ZeroDivisionError: division by zero


def test_case2():
    # with pytest.raises(Exception):
    with pytest.raises(ZeroDivisionError) as error_info:
        assert (1 / 0)  # without upper line we will get ZeroDivisionError: division by zero
    print(str(error_info))


def func():
    raise ValueError('exception func raised')



def test_case3():
    # with pytest.raises(Exception):
    with pytest.raises(Exception) as Exception_info:
        func()
    print(str(Exception_info))
    assert (str(Exception_info.value)) == 'exception func raised'