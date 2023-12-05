num = "nothing"
list1 = []
sum = 0
average = 0
count = 0

while (num != "done"):
    try:
        num = input("Please enter an integer : ")
        if (num == "done"):
            break
        else:
            num = int(num)
            list1.append(num)
            count += 1
            for n in list1:
                sum += n
            average = sum/count
            print(f"{list1} , average = {average}")
            sum = 0
    except:
        print ("invalid.input \"Please enter an integer or 'done'\"\n")
print("---------- Bye !! --------------")