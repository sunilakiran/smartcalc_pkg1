# SmartCalc MLOps

A Smart Calculator Python package with Machine Learning features, deployed end-to-end using MLOps best practices.

## Installation

You can install the package directly from PyPI:

```bash
pip install smartcalc_mlops
```

## Features
- **Basic Calculator**: Addition, subtraction, multiplication, division.
- **Advanced Math**: Power, square root, logarithm, factorial.
- **Statistics**: Mean, median, standard deviation.
- **ML Module**: Linear regression (from scratch), gradient descent, Mean Squared Error (MSE).
- **MLOps**: Custom logging system, configuration loader, and specific exceptions.

## Usage

```python
from smartcalc_mlops import Calculator, MLModule

# Basic math
calc = Calculator()
print(calc.add(2, 3))

# ML Module
ml = MLModule()
X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
slope, intercept = ml.linear_regression(X, y)
print(f"Slope: {slope}, Intercept: {intercept}")
```

# smartcalc_pkg1
simple mlops calculator to calculate 
