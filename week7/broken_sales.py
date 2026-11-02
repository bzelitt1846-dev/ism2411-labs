# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale                     # Added the + sign to make the add up all of the values rather then overriding.
    print(f"Total: ${total}")         # Tabed the beginning of the line to make it part of the for loop as designed.

count = 0
for sale in sales:                    # Added the Colon to allow the function to run properly.
    count += 1
    print(f"Count: {count}")          # Tabed the beginning of the line to make it part of the for loop as designed.

i = 0
while i < len(sales):                 # Removed the = sign in order to 
    print(sales[i])
    i += 1
