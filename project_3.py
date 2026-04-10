# **Project 3 – Odd or Even**
# **Topic:** Conditionals

# **Task:**
# Take a number from the user and print if it’s odd or even.

# **Hints:**

# * Use modulus `%` operator.
# * Use an `if-else` statement.

# **Example expected output:**

# ```
# Enter a number: 7
# 7 is odd.
# ```

# ---


while True:
    try:
        number = input("Enter a number: ")

        if number != "":
            if int(number) % 2 == 0:
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
        else:
            print("Enter a number to check")

    except ValueError:
        print("Only numbers are allowed")