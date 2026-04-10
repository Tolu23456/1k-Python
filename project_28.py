# ---

# **Project 28 – Count Vowels in String**
# **Topic:** Loops & Strings

# **Task:**
# Count number of vowels in a given string.

# **Hints:**

# * Loop through string and check if character in 'aeiou'

# **Example expected output:**

# ```
# Enter string: hello
# Number of vowels: 2
# ```

# ---

vowel = ["a", "e", "i", "o", "u"]
count = 0

input_string = input("Enter string: ")

for string in input_string:
    if string in vowel:
        count += 1

print(f"Number of vowel: {count}")
