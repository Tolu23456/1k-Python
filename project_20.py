# ---

# **Project 20 – Dictionary Merge**
# **Topic:** Dictionaries

# **Task:**
# Merge two dictionaries and print the result.

# **Hints:**

# * Use `{**dict1, **dict2}`

# **Example expected output:**

# ```
# Dict1: {'a':1}
# Dict2: {'b':2}
# Merged: {'a':1, 'b':2}
# ```

# ---

dict1 = {'a':1}
dict2 = {'b':2}

merge = {**dict1, **dict2}

print(f"Dict1: {dict1} \nDict2: {dict2} \nMerged: {merge}")