# Electricity Bill Calculator
RATE = 12.90


while True:
    name = input("Enter customer name: ")


    if name.strip() != "":
        break
else:
    print("Invalid name, please try again.")


previous = input("Enter previous meter reading: ")

if not previous.isdigit() or not (0 <= int(previous) <= 100000):
    print("Invalid previous meter reading, try again.")
    previous = input("Enter previous meter reading: ")

current = input("Enter current meter reading: ")
    
if not current.isdigit() or not (0 <= int(current) <= 100000):
    print("Invalid previous meter reading, try again.")
    current = input("Enter current meter reading: ")
  

consumption = int(current) - int(previous)
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
