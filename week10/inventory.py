# The most suprizing thing is probably that it is a base 0 system.
# This can be confusing at first, but it makes sense once you start working with it.

# Using a python list to do inventory at my cooking center could have been useful.
# Having each item in a list with corrosponding count values and condition values could be useful.

# --- Exercise 1: Build a List ---
print(" --- Exercise 1: Build a List --- ")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)  # This will return the list of items in the inventory
print(len(inventory))  # This will return 5

# --- Exercise 2: Index Practice ---

print(" --- Exercise 2: Index Practice --- ")
print(inventory[0])  # This will return the first item in the list
print(inventory[-1]) # This will return the last item in the list

middle = len(inventory) // 2
print(inventory[middle])  # grabs the middle item (not hard coded)

# --- Exercise 3: List Slicing ---

print(" --- Exercise 3: List Slicing  --- ")

print(inventory[:3])  # This will return items from index 0 to 2
print(inventory[-2:])  # This will return items from index 2 to index 4
print(inventory[::2])  # This will return every second item from the list

# --- Exercise 4: Modify ---

print(" --- Exercise 4: Modify --- ")

inventory.append("envelope")  # This will add "envelope" to the end of the list
inventory.append("tape")  # This will add another "tape" to the end of the list
print(inventory)

inventory.remove("tape")   # This will remove "tape" from the list
print(inventory)

inventory.sort()  # This will sort the list in alphabetical order
print(inventory)

# --- Exercise 5: Tuple Comparison ---

print(" --- Exercise 5: Tuple Comparison --- ")
coords = (40.7128, -74.0060)  # Coordinates of New York City

try:
    coords[0] = 99 
except TypeError as e:
    print(f"TypeError caught: {e}") 
    print("Tuples protect coordiants from being changed on accident")

# --- Exercise 6: Average of a list of sales ---

print(" --- Exercise 6: List Average Sales --- ")

sales = [100, 250, 75, 480, 200]
total = sum(sales)  # This will calculate the total sales
count = len(sales)  # This will count the number of sales
average = total / count  # This will calculate the average sales
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]
for sale in sales:
    if sale > best:
        best = sale
    if sale < worst:
        worst = sale

print(f"Best sale: {best}")
print(f"Worst sale: {worst}")

# --- Exercise 7: Accumulator pattern ---

print(" --- Exercise 7: Accumulator Pattern --- ")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list to add things to
for price in prices:
    discounted.append(round(price * 0.9, 2))  # Apply a 10% discount and round to 2 decimal places

print(prices)
print(discounted)

# --- Exercise 8: Filter  ---

print(" --- Exercise 8: Filter  --- ")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []  # an empty list to add things to <- MUST BE ON THE OUTSIDE

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")