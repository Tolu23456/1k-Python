# ---

# **Project 11 – Student Grades**
# **Topic:** Class

# **Task:**
# Create a `Student` class with attributes `name` and `grades`, and methods `add_grade()`, `average()`, `display()`.

# **Hints:**

# * Use `self.grades` to store grades.
# * `average()` should calculate mean.

# **Example expected output:**

# ```
# Student: Alice
# Grades: [80, 90, 70]
# Average: 80.0
# ```

# ---

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        print(f"Student: {self.name}\nGrades: {self.grades}")
        return f"Average: {sum(self.grades) / len(self.grades)}"

s1 = Student("Tolu", [80, 90, 70])
print(s1.average())