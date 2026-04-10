# ---

# **Project 13 – Even Numbers List**
# **Topic:** Loops

# **Task:**
# Print all even numbers from 1 to `n`.

# **Hints:**

# * Use `range()` with step 2 or modulus `%`.

# **Example expected output:**

# ```
# Enter n: 10
# Even numbers: 2 4 6 8 10
# ```

# ---

n = int(input("Enter n: "))

for even in range(1, n):
    if even % 2 == 0:
        print(f"Even numbers: {even}")