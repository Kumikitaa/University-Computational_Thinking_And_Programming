word = "nothing";

word = str(input("Enter string : "));
print (f"\nInput string = {word}\n");

length = len(word) - 1;

while (length >= 0):
    print (word[length], "\n");
    length -= 1;