
def test_a1():
    print('first test case')
    assert  5 + 5 == 10

def test_a2():
    print('second test case')
    assert  'abcd' == 'abcd'

def test_a3():
    print('third test case')
    assert  True

def test_a4():
    assert  1 in divmod(9,5) # returns (9/5,9%5)


def test_a5():
    assert  'py' in 'pytest'
