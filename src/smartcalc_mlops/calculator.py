from .exceptions import MathError
from .logger import get_logger

logger = get_logger("Calculator")

class Calculator:
    """Basic calculator operations."""
    
    def add(self, a, b):
        logger.info(f"Adding {a} and {b}")
        return a + b
        
    def subtract(self, a, b):
        logger.info(f"Subtracting {b} from {a}")
        return a - b
        
    def multiply(self, a, b):
        logger.info(f"Multiplying {a} and {b}")
        return a * b
        
    def divide(self, a, b):
        logger.info(f"Dividing {a} by {b}")
        if b == 0:
            logger.error("Division by zero attempted.")
            raise MathError("Cannot divide by zero.")
        return a / b
