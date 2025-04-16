
from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(2.5, 3.5) == 6.0
    assert add(2, -3) == -1
    assert add(-2, 3) == 1
    
