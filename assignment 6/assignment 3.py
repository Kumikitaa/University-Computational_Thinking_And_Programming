fname = input("Enter a file name : ");
average = 0;
count = 0;
sum = 0;

try:
    fhand = open (fname);
except:
    print (f"\nFile cannot be opened: {fname}");
else:
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            pos1 = line.find(":");
            pos2 = line.find("\n");
            num = float(line[pos1+2:pos2]);
            sum += num;
            count += 1;
    average = sum / count;
    fhand.close()
    print (f"Average spam confidence: {average}");