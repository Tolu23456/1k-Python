# ---

# **Project 2 – Age Checker**
# **Topic:** Datatypes

# **Task:**
# Ask the user for their age and tell them if they are a child, teen, adult, or senior.

# **Hints:**

# * Use integers for age.
# * Use `if-elif-else` to determine category.

# **Example expected output:**

# ```
# Enter your age: 16
# You are a teenager.
# ```

# ---

"""
Using my range chain rule which state that the value of the variable must be less than or equal to the upper limit and greater than the lower limit, I can determine the age category of the user.
min_value <= variable < max_value
"""


print("\n-____Age Tracker____-")

while True:
    age = int(input("\nEnter your age: "))

    if 1 <= age < 13:
        print("You are a kid")
    elif 13 <= age < 20:
        print("You are a teen")
    elif 20 <= age < 50:
        print("You are an adult")
    elif 50 <= age < 120:
        print("You are a senior")
    elif 120 <= age < 1_001:
        print("You are very old")
    elif age > 1_001:
        print("Humans doesn't live that long")
    else:
        print("Invalid age")