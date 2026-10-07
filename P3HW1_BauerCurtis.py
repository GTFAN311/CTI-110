# Curtis Bauer
# 6 Oct 2026
# P3HW1
# Debugging assignment

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low_grade = min(grades)
high_grade = max(grades)
sum_grade = sum(grades)
average_grade = sum(grades)/6   

#Show the results
sym = "-"
line = sym * 12
end = sym * 40
print(line,"Results",line)
print(f"{'Lowest Grade: ':<20}{low_grade:.1f}")
print(f"{'Highest Grade: ':<20}{high_grade:.1f}")
print(f"{'Sum of Grades: ':<20}{sum_grade:.1f}")
print(f"{'Average: ':<20}{average_grade:.2f}")
print(end)

# determine letter grade for average

if average_grade >= 90:
    print('Your grade is: A')
    
elif average_grade >= 80:
    print('Your grade is: B')

elif average_grade >= 70:
    print('Your grade is: C')
   
elif average_grade >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')

