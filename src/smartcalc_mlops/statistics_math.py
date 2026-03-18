import statistics
from .exceptions import MathError
from .logger import get_logger

logger = get_logger("StatisticsMath")

class StatisticsMath:
    """Statistical operations."""
    
    def _check_list(self, data):
        if not data:
            logger.error("Empty data list provided.")
            raise MathError("Data list cannot be empty.")
            
    def mean(self, data):
        logger.info(f"Calculating mean of {len(data)} items")
        self._check_list(data)
        return statistics.mean(data)
        
    def median(self, data):
        logger.info(f"Calculating median of {len(data)} items")
        self._check_list(data)
        return statistics.median(data)
        
    def std(self, data):
        logger.info(f"Calculating standard deviation of {len(data)} items")
        self._check_list(data)
        if len(data) < 2:
            logger.error("Standard deviation requires at least 2 data points.")
            raise MathError("Standard deviation requires at least two data points.")
        return statistics.stdev(data)
