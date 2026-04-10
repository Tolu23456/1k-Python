fruits = ["Apple", "Banana", "Pineapple", "Watermelon", "Orange"]

search = input("Search: ").capitalize()

if search in fruits:
    print("Yes, we have that!")
else:
    print("Sorry, out of stock.")