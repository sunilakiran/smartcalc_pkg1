import math
from .exceptions import MathError
from .logger import get_logger

logger = get_logger("AdvancedMath")

class AdvancedMath:
    """Advanced mathematical operations."""
    
    def power(self, base, exponent):
        logger.info(f"Calculating {base} to the power of {exponent}")
        return math.pow(base, exponent)
        
    def sqrt(self, number):
        logger.info(f"Calculating square root of {number}")
        if number < 0:
            logger.error("Square root of negative number attempted.")
            raise MathError("Cannot calculate square root of a negative number.")
        return math.sqrt(number)
        
    def log(self, number, base=math.e):
        logger.info(f"Calculating logarithm of {number} with base {base}")
        if number <= 0:
            logger.error("Logarithm of non-positive number attempted.")
            raise MathError("Logarithm undefined for non-positive numbers.")
        return math.log(number, base)
        
    def factorial(self, n):
        logger.info(f"Calculating factorial of {n}")
        if not isinstance(n, int) or n < 0:
            logger.error("Factorial of non-negative integer attempted.")
            raise MathError("Factorial only defined for non-negative integers.")
        return math.factorial(n)
