
class TestMyStuff():
    def test_type(self):
        assert  type(1) == int

    def test_strs(self):
        assert  str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'


# (venv) D:\mine\Python Automation Testing With Pytest\Pytest-Automation>pytest -v -s Pytest_topics\py_assertions\test_module02.py::TestMyStuff::test_strs
