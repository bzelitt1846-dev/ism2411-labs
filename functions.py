# Self Assessment 
#   1. The first bug I spotted was the missing : on the 10th line. I found it before I did the traceback. It tells me that I am capable of 
# finding bugs in my code but that I will probably still need to use the traceback to find some of the more difficult bugs. 
#   2. apply_discount(price, tier) is a function that describes the discount that will be applied based on the price inputed and the tier inputed. 
# I believe anyone could use it if I made the input request obvious enough to understand. 
#   3. The only use of AI that I used besides the requested traceback, was VSCodes auto complete in order to speed up my coding.
# I was in class when we went over the lab and I followed everything as shown but partially auto completed by the AI in VSCode. 

# --- Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 ---

# Defining a function with 
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # 15% discount
    elif tier == "silver":
        return price * 0.90  # 10% discount
    elif tier == "bronze":
        return price * 0.95  # 5% discount
    else:
        return price  # No discount for other tiers

# Calling the function
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: $ {apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the function
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

# --- Exercise 5 --- 

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
while i < len(sales):                 # Removed the = sign in order to allow the last value in the list to be printed.
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100 # Global variable

def double_it():
    x = 999 # Local variable
    return x * 2

print(x) # 100
print(double_it()) # 1998
print(x) # 100
