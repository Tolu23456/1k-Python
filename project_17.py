# ---

# **Project 17 – Count Characters in String**
# **Topic:** Datatypes

# **Task:**
# Ask user for a string and count number of characters.

# **Hints:**

# * Use `len()` function.

# **Example expected output:**

# ```
# Enter string: hello
# Length: 5
# ```

# ---

string = input("Enter string: ")
count = 0

for n in string:
    count += 1

print(f"Length: {count}")