#Curtis Bauer
#15 Sep 2026
#P1HW2
#Travel Expenses

#Calculates a budget for a trip

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter budget: "))
print()

loc = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

hotel = int(input("Approximately, how much will you need for accomodations/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

print("--------Travel Expenses--------")
print("Location: ", loc)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
exp = int(gas + hotel + food)
bal = int(budget - exp)
print("Remaining Balance: ", bal)