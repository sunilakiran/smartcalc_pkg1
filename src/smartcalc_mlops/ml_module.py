from .exceptions import MLModelError
from .logger import get_logger

logger = get_logger("MLModule")

class MLModule:
    """Machine learning operations."""
    
    def mse(self, y_true, y_pred):
        logger.info(f"Calculating MSE for {len(y_true)} predictions")
        if len(y_true) != len(y_pred):
            raise MLModelError("y_true and y_pred must be of the same length.")
        if not y_true:
            raise MLModelError("Input lists cannot be empty.")
            
        sum_squared_error = sum((t - p) ** 2 for t, p in zip(y_true, y_pred))
        return sum_squared_error / len(y_true)
        
    def gradient_descent(self, X, y, learning_rate=0.01, epochs=1000):
        """Simple gradient descent for 1D linear regression: y = mX + b"""
        logger.info(f"Running gradient descent for {epochs} epochs")
        if len(X) != len(y) or not X:
            raise MLModelError("X and y must be non-empty and of same length.")
            
        m = 0.0
        b = 0.0
        n = len(X)
        
        for _ in range(epochs):
            y_pred = [m * x + b for x in X]
            
            # Gradients
            dm = (-2 / n) * sum(x * (yt - yp) for x, yt, yp in zip(X, y, y_pred))
            db = (-2 / n) * sum(yt - yp for yt, yp in zip(y, y_pred))
            
            m -= learning_rate * dm
            b -= learning_rate * db
            
        return m, b
        
    def linear_regression(self, X, y):
        """Closed-form solution for 1D linear regression."""
        logger.info("Computing linear regression (closed-form)")
        if len(X) != len(y) or not X:
            raise MLModelError("X and y must be non-empty and of same length.")
            
        n = len(X)
        mean_X = sum(X) / n
        mean_y = sum(y) / n
        
        numerator = sum((x - mean_X) * (y_item - mean_y) for x, y_item in zip(X, y))
        denominator = sum((x - mean_X) ** 2 for x in X)
        
        if denominator == 0:
            raise MLModelError("Cannot compute regression, all X values are identical.")
            
        m = numerator / denominator
        b = mean_y - m * mean_X
        
        return m, b
