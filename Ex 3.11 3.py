#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

scr=input("Enter Score:")
try:
    X=float(scr)
except:
    print("Incorrect Value")
    quit()
if X<1.0:
    if X>=0.9:
        print('A')
    elif X>=0.8:
        print('B')
    elif X>=0.7:
        print('C')
    elif X>=0.6:
        print('D')
    elif X<0.6:
        print('f')
else:
    print("Please Enetr a correct score")
