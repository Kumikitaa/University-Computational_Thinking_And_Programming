word = "nothing";

while (word != "done"):
    word = str(input("Please enter string : "));
    if (word == "done"):
        print ("\nBye !");
    else:
        list1 = list(word);
        length = len(list1);
        index1 = length - 1;
        index2 = 0;
        new_word = "";
        while (index2 <= index1):
            if (list1[index2] == ",") or (list1[index2] == ".") or (list1[index2] == ":") or (list1[index2] == "!") or (list1[index2] == "?"):
                new_word = new_word;
            else:
                new_word = new_word + list1[index2].upper();
            index2 += 1;
        print (f'\n{new_word}\n');