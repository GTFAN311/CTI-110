# Curtis Bauer
# 6 Oct 2026
# P3HW2
# Employee Pay Stub

# Gather data from user
empname = input("Enter employee's name: ")
hrswork = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))
sym = "-"
div = sym *37
print(div)

# Display employee name
print(f"{'Employee name: ':<17}{empname}")
print()

# if/else statements
if hrswork > 40:
    reghrs = 40
    othrs = hrswork -40
else:
    reghrs = hrswork
    othrs = 0.0
    
# Calculate/display hours worked and pay earned
otrate = pay *1.5
regpay = reghrs *pay
otpay = othrs *otrate
grpay = regpay + otpay
div2 = sym *98 
    
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<20}{'Reg Hour Pay':<20}{'Gross Pay':<20}")
print(div2)
print(f"{hrswork:<15}{pay:<12}{othrs:<15}{otpay:<20.2f}{regpay:<20.2f}{grpay:<20.2f}")