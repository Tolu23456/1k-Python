# ---

# **Project 10 – Contact Book**
# **Topic:** Dictionaries

# **Task:**
# Store names and phone numbers in a dictionary and allow the user to search by name.

# **Hints:**

# * Use `dict.get()` to safely get values.

# **Example expected output:**

# ```
# Enter name to search: Bob
# Phone: 123-456-7890
# ```

# ---

contact = {
    "Bob": "123-456-7890",
    "Tolu": "09115170518"
}

search = input("Enter name to search: ")

if search in contact:
    print(f"Phone: {contact.get(search)}")