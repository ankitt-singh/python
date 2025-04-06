#Syntex
"""
if(Condition):
   statment1
elif(Condition):
   statment2
else:
   condition3
"""

#Traffic light
light = input("What is the color of the Siginal")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Be Redy")
elif(light == "green"):
    print("go")
else:
    print("Signal is not working")

# Write a Program to input 2 numbers and print their sum.
num1 = int(input("enter the first number:"))
num2 = int(input("Enter the second number:"))
sum = num1 + num2
print(sum)

# WAP to take input side of a square and print its area
Side = int(input("Enter the side of the Square:"))
Area = Side * Side
print(Area)

# WAP to input 2 floating points and print their average
f1 = float(input("Enter the firat num:"))
f2 = float(input("enter the second num"))
avg = (f1 + f2) / 2
print(avg)

#WAP to input 2 int numbers, a and b
#print True if a is greater then or equa to b. if not print false
num3 = int(input("Enter the first num"))
num4 = int(input("Enter the second number:"))

print(num3 >= num4)
# if(num3 >= num4):
#     print("True")
# else:
#     print("False")