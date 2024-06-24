import pytest

# Assuming the add function is in a module named `main`
from main import add

def test_add():
    """Test the add function"""
    assert add(1, 2) == 3, "Expected add(1, 2) to be 3"
    assert add(-1, 1) == 0, "Expected add(-1, 1) to be 0"
    assert add(0, 0) == 0, "Expected add(0, 0) to be 0"
    assert add(-1, -1) == -2, "Expected add(-1, -1) to be -2"
    assert add(1.5, 2.5) == 4.0, "Expected add(1.5, 2.5) to be 4.0"
    assert add(1, -2) == -1, "Expected add(1, -2) to be -1"

if __name__ == "__main__":
    pytest.main()
