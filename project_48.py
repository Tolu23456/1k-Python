"""
Grocery Adder: Add items to a list.
   - Hint: Use .append().
   - Components: items list.
"""

list_items = []
i = 0

while i < 3:
    item = input("Item: ").capitalize()
    list_items.append(item)
    i += 1
print(f"Your grocery list: {list_items}")