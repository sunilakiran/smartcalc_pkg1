import pytest
from smartcalc_mlops.statistics_math import StatisticsMath
from smartcalc_mlops.exceptions import MathError

def test_mean():
    stat = StatisticsMath()
    assert stat.mean([1, 2, 3, 4, 5]) == 3.0

def test_median():
    stat = StatisticsMath()
    assert stat.median([1, 3, 3, 6, 7, 8, 9]) == 6.0

def test_std():
    stat = StatisticsMath()
    assert round(stat.std([1, 2, 3, 4]), 2) == 1.29

def test_empty_list():
    stat = StatisticsMath()
    with pytest.raises(MathError):
        stat.mean([])

def test_std_single_item():
    stat = StatisticsMath()
    with pytest.raises(MathError):
        stat.std([1])
