"""
Unique List: Remove duplicates from a list.
   - Hint: Convert to set() then back to list().
   - Components: original, unique.
"""


duplicate_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = list(set(duplicate_list))

print(unique_list)