"""
Identity Match: Check if names match (ignore case).
   - Hint: Use .lower() then ==.
   - Components: name1, name2.
"""

system_name = "Tolu"

name = input("Enter name: ").capitalize()

if name == system_name:
    print("Identity Verified.")
else:
    print("Unknown User.")