count = 0;
sum = 0;
average = 0;
num = "repeat";

print("To finish counting please write \"done\"");

while(num != "done"):
    try:
        num = input("\nEnter a number: ");
        num = float(num);
        if (num != "done") and (type(num) == float): 
            sum += num;
            count += 1;
    except:
        if num != "done":
            print("invalid.input please enter numeric input\n");
        else:
            break;

if sum != 0:
    average = float(sum / count);
    sum = int(sum);

print("\nSum of input number:", sum);
print("numbers of input:", count);
print("Average of input numbers:", average);