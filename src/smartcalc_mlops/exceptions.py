class SmartCalcException(Exception):
    """Base exception for smartcalc_mlops."""
    pass

class MathError(SmartCalcException):
    """Raised for mathematical errors like division by zero."""
    pass

class MLModelError(SmartCalcException):
    """Raised for errors within the ML Module."""
    pass
