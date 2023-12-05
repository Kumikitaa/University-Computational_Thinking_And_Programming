score = "error"; # I am using string type for while statement

#checking for valid input:
while(type(score) != float or (score < 0) or (score > 100)):
    try:
        score = float(input("Enter Score: "));
        if (score < 0) or (score > 100):
            print("invalid.input \"Please enter numeric input between 0 and 100\"\n");
    except:
        print("invalid.input \"Please enter numeric input between 0 and 100\"\n");

#output:
if score >= 90:
    grade = 'A';
elif score >=80:
    grade = 'B';
elif score >= 70:
    grade = 'C';
elif score >= 60:
    grade = 'D';    
else:
    grade = 'F';
print("Grade is %s" %grade);