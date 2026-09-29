# Curtis Bauer
# 29 Sept 2026
# P2HW2
# Calculate grades

# Inputs for Modules
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

# Grades set
grades = [65.5, 88, 78.5, 90, 61, 92]

# Grade caluculations
lowest_grade = min(grades)
highest_grade = max(grades)
sum_grade = sum(grades)
average_grade = sum(grades)/6

#Show the results
sym = "-"
line = sym * 12
end = sym * 40
print(line,"Results",line)
print(f"{'Lowest Grade: ':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade: ':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades: ':<20}{sum_grade:.1f}")
print(f"{'Average: ':<20}{average_grade:.2f}")
print(end)