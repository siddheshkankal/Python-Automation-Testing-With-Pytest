# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

def test_a1():
    print('first test case')
    assert  5 + 5 == 10


def test_a2():
    assert  9/5 == 1.8,"failed test"

def test_a3():
    assert  9//5 == 1,"failed test a3"

# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -s Pytest_topics\test_module01.py::test_a1

