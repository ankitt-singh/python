# concatenation in string: (+)
str1 = "Hello my name is Ankit Singh."
str2 = "hi I am Suraksha."
print(str1 + " " + str2)

# finding the length of a string: (len())
print(len(str1))

#Slicing
print(str2[2 : 6])

#str.endsWith()
print(str1.endswith("Singh."))

#str.replace(old,new)
print(str1.replace("Ankit", "Anish"))
print(str1)

#str.capitalize()
print(str2.capitalize()) #captalize only first char

#str.find("word")
print(str2.find("Suraksha"))

#str.count("word")
print(str1.count("o"))

# practice problem

# WAP to input user's first name and print its length
user1 = input("Enter your name:  ")
print(len(user1))

# WAP to find the occurrence of "s" in string
print(user1.count("s"))