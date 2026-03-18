import pytest
import math
from smartcalc_mlops.ml_module import MLModule
from smartcalc_mlops.exceptions import MLModelError

def test_mse():
    ml = MLModule()
    assert ml.mse([1, 2, 3], [1, 2, 3]) == 0.0
    assert ml.mse([1, 2], [2, 3]) == 1.0

def test_mse_length_mismatch():
    ml = MLModule()
    with pytest.raises(MLModelError):
        ml.mse([1, 2], [1])

def test_linear_regression():
    ml = MLModule()
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    m, b = ml.linear_regression(X, y)
    assert 0 < m < 1.0 # m is roughly 0.6
    assert 1.0 < b < 3.0 # b is roughly 2.2

def test_linear_regression_error():
    ml = MLModule()
    with pytest.raises(MLModelError):
        ml.linear_regression([1, 1, 1], [1, 2, 3])

def test_gradient_descent():
    ml = MLModule()
    X = [1, 2, 3]
    y = [2, 4, 6]
    m, b = ml.gradient_descent(X, y, epochs=100)
    # very rough estimates for small epochs
    assert m > 0
