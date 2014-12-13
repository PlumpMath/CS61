"""
Code Writer : EOF
Code file   : exercise_2.py
Code date   : 2014.12.13

Exercise 2: Control Flow

"""
a = 1
b = 2

"""
Boolean operator
"""
print("Output of the part of boolean operator\n")

print("a > b and a == 0")
print(a > b and a == 0)

print("a > b or a == 0")
print(a > b or a == 0)

print("not a == 0")
print(not a == 0)

"""
if statements
"""
print("\n\n\n Outout of if statements")

if a == b:
     print(a)
else:
     print(b)

"""
while loops
"""

n = 4;
def countDown(n):
    while(n > 0):
         print(n)
         n = n -1;

countDown(5)
