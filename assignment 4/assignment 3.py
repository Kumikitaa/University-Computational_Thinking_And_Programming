num = "nothing"; # I am using string type for while statement

#function with numbers which can be divided by 3 
def num_divide3(num):
    n = 0;
    for i in range (1, num + 1):
        if ((i % 3) == 0):
            n += 1;
    return n;

#main function
while (num != "done"):
    try:
        num = input("Please enter a positive integer: ");
        if (num != "done"): # checking if process is not done
            num = int(num);
        else:
            print("bye !!");
            break;
        if (num <= 0): # checking if input is positive integer
            print("invalid.input \"please enter a positive number\"\n");
        elif __name__ == "__main__":
            print("Numbers divisible by 3 among numbers from 1 to", num, ":", num_divide3(num), "\n");
    except:
        print ("invalid.input \"please enter a positive number\"\n");