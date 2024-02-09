##import pytest
from math_utils import MathUtils

@pytest.fixture
def math_utils_instance():
    """Fixture to create an instance of MathUtils for testing."""
    return MathUtils()

def test_addition():
    assert MathUtils.add(3, 5) == 8
    assert MathUtils.add(-2, 7) == 5
    assert MathUtils.add(0, 0) == 0

def test_subtraction():
    assert MathUtils.subtract(10, 4) == 6
    assert MathUtils.subtract(-5, 3) == -8
    assert MathUtils.subtract(0, 0) == 0

def test_multiplication():
    assert MathUtils.multiply(3, 4) == 12
    assert MathUtils.multiply(-2, 5) == -10
    assert MathUtils.multiply(0, 7) == 0

def test_division(math_utils_instance):
    assert MathUtils.divide(8, 2) == 4.0
    assert MathUtils.divide(10, 3) == pytest.approx(3.333, abs=1e-3)  # Approximate equality
    assert MathUtils.divide(-6, 2) == -3.0

    # Test division by zero
    assert MathUtils.divide(5, 0) == -1.0

