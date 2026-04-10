"""
The "Not" Checker: "Access Denied" if user is "Banned".
   - Hint: Use != or "not" keyword.
   - Components: status.
"""

status = input("Enter status: ").capitalize()

positive_status = ["Active", "Guest"]
negative_status = ["Banned"]


if status in positive_status:
    print("Access Granted!")
elif status in negative_status:
    print("Access denied!")
else:
    print("Try again!")