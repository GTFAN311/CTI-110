#Curtis Bauer
#24 Sept 2026
#P2HW1
#Travel Expenses Improved

#Calculates a budget for a trip

print("This program calculates and displays travel expenses")
print()

# Enter budget
budget = float(input(f"Enter budget: "))
print()

# Enter travel destination
loc = input("Enter your travel destination: ")
print()

# Enter money spent for gas
gas = float(input("How much do you think you will spend on gas? "))
print()

# Enter money spent on hotel
hotel = float(input("Approximately, how much will you need for accomodations/hotel? "))
print()

# Enter money spent on food
food = float(input("Last, how much do you need for food? "))
print()

# Format output for visual appeal
sym = "-"
line = sym * 12
trav_exp = sym *40
print(line,"Travel Expenses",line)
print(f"{'Location: ':<20}{loc}")
print(f"{'Initial Budget: ':<20}${budget:.2f}")
print(f"{'Fuel: ':<20}${gas:.2f}")
print(f"{'Accomodation: ':<20}${hotel:.2f}")
print(f"{'Food: ':<20}${food:.2f}")
print(trav_exp)
print()
exp = float(gas + hotel + food)
bal = float(budget - exp)
print(f"{'Remaining Balance: ':<20}${bal:.2f}")