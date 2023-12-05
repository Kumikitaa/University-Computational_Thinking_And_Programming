# part below is used for rewriting text file in the branch
'''fhand = open ("assignment 1.txt", "w");
   for num in range (1, 20):
       text = "line number : %d\n" %num;
       fhand.write(text);
   fhand.close()'''



# part below is assignment
fname = input ("Enter a file name : ");
try:
    fhand = open (fname);
except:
    print ("\nThe file, which you entered, doesn't exist")
else:
    print ();
    for line in fhand:
        line = line.rstrip().upper();
        print (line);
    fhand.close();