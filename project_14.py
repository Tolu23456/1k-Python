# ---

# **Project 14 – Voting Eligibility**
# **Topic:** Conditionals

# **Task:**
# Ask for age and print if user can vote.

# **Hints:**

# * Voting age = 18

# **Example expected output:**

# ```
# Enter your age: 17
# Not eligible to vote.
# ```

# ---

voting_age = 18
user_age = int(input("Enter your age: "))

if 1 <= user_age < voting_age:
    print("Not eligible to vote.")
elif 18 <= user_age < 100:
    print("You are eligible to vote.")
else:
    print("Invalid age.")