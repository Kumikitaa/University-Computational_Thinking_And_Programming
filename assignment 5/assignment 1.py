word = "nothing";

while (word != 'done') and (word != ""):
    try:
        word = input("Please enter two words : ");
        if (word == 'done') or (word == ""):
            print ("\n--bye !!");
        else:
            list1 = word.split();
            if (len(list1) == 2):
                print (min(list1), "comes first\n");
            else:
                print ();
    except:
        print ();