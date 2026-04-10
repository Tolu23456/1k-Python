# ---

# **Project 21 – Calculator Class**
# **Topic:** Class

# **Task:**
# Create a `Calculator` class with methods `add`, `subtract`, `multiply`, `divide`.

# **Hints:**

# * Use `self` and methods for operations.

# **Example expected output:**

# ```
# Add: 5
# Subtract: 1
# Multiply: 6
# Divide: 2.0
# ```

# ---

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero!"

a = Calculator(4, 0)
print(a.add())
print(a.subtract())
print(a.multiply())
print(a.divide())