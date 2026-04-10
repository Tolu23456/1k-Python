"""

This is project 34. In this project am gonna solidify my knowledge on python conditions, so am gonna be working on python chain conditions and how to write better conditions.

So am gonna be creating a voting system using a function and a dictionary for storing their infos

"""

voters_dict: dict() = {}
voters_allowed: int = 0

while voters_allowed < 2:
    voters_allowed += 1

    name: str = input("Enter your name: ").capitalize()
    age: int = int(input("Enter your age: "))


    def voting_system(name: str, age: int):
        if 17 <= age <= 100:
            voters_dict[name] = age
            return f"{name} has been added to voters_dict"
        else:
            return f"{name} cannot be added because age too small"

voting_system(name, age)

print(voters_dict)
    