# Self Assessment: Sales Loop

# 1. Initialize a variable before the loop. The variable needs a starting value
# that doesn't change the answer, so 0 for sums and 1 for products. If you skip this
# Python will raise an error because total doesn't exist yet.If you put it inside the loop,
# it resets every pass and you only get the last item.

# 2. Personally, the code is much smaller but more complex to understand.
# Most code we have writen prior can be understood by just speaking out loud but this looping
# version does not follow that same idea.
 
# 3. My job this summer involved inventorying a few hundred differnet types of items and asking 
# how many we would want next year. One list would contain the item name and the other would contain
# the quantity. If I made a program that I could input the item name and quantity, it would display 
# the item and the quantity back to back.

# Exercise 1

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Exercise 2

count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# Exercise 3

current_max = 0

for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Biggest Sale: ${current_max}")

# Exercise 4

sales_over_100 = 0
total_over_100 = 0

for sale in sales: 
    if sale > 100:
        sales_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {sales_over_100}")
print(f"Total of sales over $100: ${total_over_100}")

# Exercise 5

for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
print(f"${sale}")

# Exercise 6

i = 0 

while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total sales: ${total}")

# Exercise 7

discount = 0

for sale in sales:
    if sale >= 500:
        discount = .15
    elif sale >= 200:
        discount = .10
    elif sale >= 100:
        discount = .05
    else:
        discount = 0

    final = sale * (1 - discount)
    print(f"Sale: ${sale:.2f}")
    print(f"Discount: {discount*100:.0f}%")
    print(f"Final: ${final:.2f}")