hours = "nothing";
rate = "anything"; # I am using string type for while statement

#function which calculates salary
def computepay (hours, rate):
    if(hours > 40):
        overPaidHours = hours - 40;
        remaining_hours = hours - overPaidHours;
        pay = (remaining_hours * rate) + (overPaidHours * rate * 1.5); # I know presedence, but this form is more readable
    else:
        pay = hours * rate;
    return pay;
    

#checking for valid input for hours:
while(type(hours) != int or hours < 0):
    try:
        hours = int(input("Enter how many hours do you work: "));
        if (hours < 0):
            print("invalid.input \"please enter positive numeric input (without point, special characters, etc)\"\n")
    except:
        print("invalid.input \"please enter postive numeric input (without point, special characters, etc)\"\n");

#checking for valid input for rate:
while(type(rate) != float or (rate < 0)):
    try:
        rate = float(input("\nEnter what's your rate of pay (to make a decimal number please use point (e.g. 2.5 or 1.5)): "));
        if (rate < 0):
            print("invalid.input \"please enter positive numeric input (without special characters)\"\n")
    except:
        print("invalid.input \"please enter positive numeric input (without special characters)\"\n");

if __name__ == "__main__":
    print("\nPay :", computepay (hours, rate));