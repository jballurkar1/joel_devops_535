class MathUtils:
    @staticmethod
    def add(a, b):
        """Return the sum of two integers, a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the result of subtracting b from a."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Return the result of dividing a by b.
        Ensure that division by zero is handled appropriately by returning -1.0 in such cases.
        """
        if b == 0:
            return -1.0
        return a / b

# Example usage:
result_add = MathUtils.add(5, 3)
result_subtract = MathUtils.subtract(8, 2)
result_multiply = MathUtils.multiply(4, 6)
result_divide = MathUtils.divide(10, 0)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)