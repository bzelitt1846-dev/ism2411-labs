# 1. The program takes `order_total = 350` and checks the first condition, "is it 500 or more?", which is false,
# so that top-tier discount is skipped. It then checks the next condition, "is it more than 200 and less than 500?",
# which is true, so the middle-tier discount applies. Python runs only that one branch, 
# so 350 becomes 315 after a 10% discount, and the remaining branches never run.

# 2. `if total > 200 and total < 500:` is a single test that passes only when both conditions are true at once, 
# so it selects one band of values. Two separate `if` statements would each be checked independently, and if both 
# are true, the code inside both runs. A total of 600 passes the first `if` and would run its code, even though it 
# doesn't belong in the 200 to 500 band. Two separate ifs only match the combined version if you nest one inside 
# the other, which is what `and` does for you anyway.

# 3. Tax brackets are a clear example: each slice of income is taxed at a different rate depending on which band 
# it falls in. Shipping fees, insurance premiums by age or risk group, and credit card rewards also work as conditional 
# rules. Knowing conditionals makes these systems look less mysterious and more like a chain of `if/elif` checks, 
# which makes it easier to spot edge cases, like the dollar amount right at a threshold, and to see how a small 
# change in the order of the conditions could change the outcome.

# Exercise 1

total = float(input("Enter cart total: $"))

# Add your if/elif/else statement
if total >= 500:
    discount = .15
elif total >= 200:
    discount = .10
elif total >= 100:
    discount = .05
else :
    discount = 0


final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

# Exercise 2

if final > 1000: # Strictly greater than
    status = "manager_approval_required"
else:
    status = "auto_approved"

# print(f"Status: {status}")

# Exercise 3

region = input("Enter region: ")

if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Regional bonus applied: additional 2% off")
else:
    extra_discount = 0

final = total * (1 - (discount + extra_discount))
print(final)

# Exercise 4

customer_type = input("Enter customer type: ")

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03
    print("Customer type bonus applied: additional 3% off")

# Exercise 5

amount = float(input("Enter amount: "))

if amount <= 0:
    print("Suspicious")
elif amount < 10000:
    print("Normal")
else:
    print("Large: review required")

# Exercise 6

total_spent_this_year = float(input("Enter total spent this year: $"))
orders_this_year = int(input("Enter number of orders this year: "))
has_outstanding_balance = input("Does the customer have an outstanding balance? (yes/no): ").strip().lower() # False

vip_upgrade = True

if total_spent_this_year > 2000 or orders_this_year > 10 and has_outstanding_balance == "no":
    vip_upgrade = True
else:
    vip_upgrade = False
print(f"VIP upgrade: {vip_upgrade}")