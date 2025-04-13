# A built-in data type that lets us create immutable sequences of values.

tup = ("Ankit", "Rahul", "Soun", "Monu")
print(tup[0])

# we have to put a comma at last if we have to add single element in the tuple
tup1 = ("Ankit",)
print(type(tup1))

# Methods in tuples

#tup.index() - Gives the index of the element
print(tup.index("Soun"))

#tup.count() - gives the number of occurrence of that number 
print(tup.count("Ankit"))

# Practice Question

# WAP to count the number of students with the "A" grade in the following tuples

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# Store the above value in a list and sort them from "A" to "D"

newGrade = ["C","D","A","A","B","B","A"]
newGrade.sort()
print(newGrade)
