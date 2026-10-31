#Curtis Bauer
#30 Oct 2026
#P4HW2
#Salary calculator with loops

# Gather data from user
name = input("Enter employee's name or 'done' to finish: ")

# Create accumulator variables for ot pay, reg pay, gross pay and emp count
otpay_total = 0
regpay_total = 0
grpay_total = 0
emp_total = 0

while name != 'done':
    #Add emp count plus 1
    emp_total += 1
    #Ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))


# Evaluate overtime
    if hours > 40:
        othrs = hours - 40
        otpay = othrs * (rate * 1.5)
        regpay = 40 * rate
        grpay = regpay + otpay
    else:
        otpay = 0
        othrs = 0
        regpay = hours * rate
        grpay = regpay
        
    # Add accumulator variables
    otpay_total += otpay
    regpay_total += regpay
    grpay_total += grpay
    
    
    

    # Display results for this employee    
    print("-------------------------------")
    print("Employee Name: ", name)
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<17}")
    print("--------------------------------------------------------------------")
    print(f"{hours:<15}{rate:<12}{otpay:<15}{grpay:<15}")

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees entered: ", emp_total)
print("Total amount paid for overtime: $", format(otpay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regpay_total, ',.2f'))
print("Total amount paid for gross pay: $", format(grpay_total, ',.2f'))