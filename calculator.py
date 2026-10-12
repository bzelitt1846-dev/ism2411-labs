# Revenue, Margins and Discount Calculator
# The missing /100: Python wouldn't crash, because multiplying two numbers is always a legal operation — it just produces a silently wrong answer.
# Using 10 instead of 0.10 takes ten times the price off, so a $99 item comes out to -$891.00, formatted cleanly with a dollar sign and two decimals as if it were correct.
# The only defense is a sanity check on the result, like flagging any negative final price.
# Another modulo scenario: Shift scheduling — with 47 volunteers and 6 per shift, 47 // 6 gives you 7 fully staffed shifts and 47 % 6 tells you 5 people are left over.
# The remainder is the part that needs a human decision: standby, floaters, or a short-staffed eighth shift.
# The same pattern covers eggs into cartons, records into pages, and passengers into vans.
# On the confidence question: That one's yours to answer, but the usual shaky spots at the end of Module 04 are type conversion (input() hands you a string, so input("Price: ") * 2 repeats the text instead of doubling the number), the difference between / and //, and what format specs like :.2f actually do.
# The cheapest fix is ten minutes in a Python shell typing deliberately wrong things — "5" * 3, then int("5") * 3, then -7 // 2.
# You learn the rule much faster from a wrong answer you predicted than a right one you read.

# Exercise 1

given_price = 50
quantity = 12
revenue = given_price * quantity
print(f"Revenue: ${revenue:,.2f}")



# Exercise 2

cost = 32
price = 50
margin = (price - cost) / price # Margin stays as decimal
print(f"Margin: {margin:.1%}")

# Evercise 3: Boolean Logic
# Product A wins if margin_a > margin_b
# Product A margin 60%, Product B margin (80-60)/80 = 25%
margin_a = 0.60
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3 # Remember to review basic logic operators: and, or, not

price = 150
margin = 0.35
is_premium = price > 100 and margin > 0.3 # Remember to review basic logic operators: and, or, not

# Exercise 5: Division + Mod

print(17/5) # 3.4 (True Division)
print(17//5) # 3 (Floor Division)
print(17%5) # 2 (Modulo)

dividend = 20

# Exercise 6: Full Pricing Calculator

def calc_discount(price, rate):
    return price * (1 - rate) # gives up the answer

discounted_pct = 20 
discounted_rev = revenue * ((1 - discounted_pct) / 100) # gives up the answer

print(f"Discounted Revenue: ${discounted_rev}")

# inputs name, retail_price, cost, quantity_sold, discount_rate (Whole number 0-100)

product = input("Enter the Product Name: ")
retail_price = float(input("Enter the Retail Price: "))
quantity_sold = int(input("Enter the Quantity Sold: "))
discount_rate = float(input("Enter the Discount Rate (0-100): "))
cost = float(input("Enter the Cost: "))
print("========================================")
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1 - discount_rate / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

# Output
print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")

# Exercise 7: 

BOX_SIZE = 24 # ALL UPPER CASE MEANS CONSTANT (NEVER CHANGES)
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE # Floor division is not abstract math
loose_items = items_ordered % BOX_SIZE # Modulo is not abstract math
exact_fit = loose_items == 0
print(f"Full Boxes: {full_boxes}")
print(f"Loose Items: {loose_items}")
print(f"Exact Fit: {exact_fit}")

# Stretch Goals: 
# A
retail_price = 50
cost = 32
fixed_costs = 10000.0
contribution = retail_price - cost
whole_units = int(fixed_costs // contribution)
print(f"Whole Units: {whole_units}")
