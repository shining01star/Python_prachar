#3 ways to write this program in one line- 

#1 by using temporary variable - \
a,b = 5,9; print(f"Original values: a = {a}, b = {b}")
temp=a; a=b; b=temp; print(f"swapped values: a = {a}, b= {b}")

#2 by using lambda function
a,b = 7,3; print(f"Original values: a = {a}, b = {b}"); a,b = (lambda x,y:(y,x))(a,b); print(f"swapped values: a = {a}, b= {b}")

#3 without using temp variable
a,b = 4,6; a,b = b,a; print(f"swapped values: a={a}, b = {b}")
