hours = "nothing";
rate = "anything"; # I am using string type for while statement

#while statement for hours:
while(type(hours) != int):
    input_hours = input("Enter how many hours do you work: ");
    try:
        hours = int(input_hours);
    except:
        print("invalid.input \"please enter numeric input (without point, special characters, etc)\"\n");

#while statement for rate:
while(type(rate) != float):
    input_rate = input("\nEnter what's your rate of pay (to make a decimal number please use point (e.g. 2.5 or 1.5)): ");
    try:
        rate = float(input_rate);
    except:
        print("invalid.input \"please enter numeric input (without special characters)\"\n");

#calculating salary
if(hours > 40):
    overPaidHours = hours - 40;
    remaining_hours = hours - overPaidHours;
    salary = (remaining_hours * rate) + (overPaidHours * rate * 1.5); # I know presedence, but this form is more readable
else:
    salary = hours * rate;
print("\nYou will be paid", salary);