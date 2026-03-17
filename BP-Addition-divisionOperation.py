#Write a Python program to do arithmetical operations addition and division.
''' pseudocode - ask a num from user and then add them easily.
1. float --> to handle the decimel values
2. input() --> function for getting input from user.
'''
#Now three methods are there
#simpler one- 
a = float(input("Enter first number: "))
b = float(input("Enter second number: ")) 
print("addition is: ", a+b)

#advance one
a == float(input("Enter first number: ")), b == float(input("Enter second number: ")), print("addition is: ", a+b)
#if you write like this, it will interprate print function as a tuple that's why we need to separate it within this line by using ; separator
#if you want to write both addition and division operation in one line- ; it is very important to separate the print statement otherwise he will interpretate everything as a tuple. 

a,b  = float(input("enter first number: ")), float(input("enter second number: ")); print("addition is: ", a+b, "division is: ", a/b)
#That's how you can write this code in one line. 
