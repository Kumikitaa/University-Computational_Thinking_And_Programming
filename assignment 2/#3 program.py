#3 program

seconds1 = int(input("Enter seconds : "));

hours = int(seconds1/3600);
minutes = int((seconds1 - hours * 3600)/60);
seconds2 = int(seconds1 - hours * 3600 - minutes * 60);

hours = str(hours);
minutes = str(minutes);
seconds2 = str(seconds2);
seconds1 = str(seconds1);

print(seconds1 + " seconds is " + hours + " hours, " + minutes + " minutes, " + seconds2 + " seconds ");