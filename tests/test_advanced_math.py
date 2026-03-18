import pytest
import math
from smartcalc_mlops.advanced_math import AdvancedMath
from smartcalc_mlops.exceptions import MathError

def test_power():
    adv = AdvancedMath()
    assert adv.power(2, 3) == 8.0

def test_sqrt():
    adv = AdvancedMath()
    assert adv.sqrt(16) == 4.0

def test_sqrt_negative():
    adv = AdvancedMath()
    with pytest.raises(MathError):
        adv.sqrt(-1)

def test_log():
    adv = AdvancedMath()
    assert math.isclose(adv.log(math.e), 1.0)
    assert adv.log(100, 10) == 2.0

def test_factorial():
    adv = AdvancedMath()
    assert adv.factorial(5) == 120

def test_factorial_negative():
    adv = AdvancedMath()
    with pytest.raises(MathError):
        adv.factorial(-5)
