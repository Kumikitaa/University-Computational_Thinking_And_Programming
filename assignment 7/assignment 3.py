count = 0

fhand = open("mbox.txt", "r")
for line in fhand:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            list1 = line.split()
            print(list1[1])
            count += 1
print(f"Total {count} lines were printed")