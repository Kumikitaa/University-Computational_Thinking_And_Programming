word = "nothing";
word = str(input("Please enter string : "));
list1 = list(word);
length = len(list1);
index = length - 1;

#all required outputs
uppercase = 0;
lowercase = 0;
numbers = 0;
other = 0;


while (index >= 0):
    if (list1[index].isalpha() == True): # letter or not
        if (list1[index].isupper() == True): # uppercase of lowercase
            uppercase += 1;
        else:
            lowercase += 1;
    elif (list1[index].isdigit() == True): # number or not
        numbers += 1;
    else:
        other += 1;
    index -= 1;


print (f"- Uppercase letters : {uppercase}");
print (f"- Lowercase letters : {lowercase}");
print (f"- Numbers : {numbers}");
print (f"- Other characters : {other}");