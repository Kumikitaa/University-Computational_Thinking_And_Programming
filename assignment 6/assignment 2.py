fhand = open ("mbox.txt", "r");
count = 0;

for line in fhand:
    if line.startswith("From:"):
        line = line.rstrip(); 
        pos = line.find("@"); # finding the position of letter after "@"
        host = line[pos+1:];
        print (host);
        count += 1;

print (f"Total {count} hosts printed");