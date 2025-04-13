# Dictionary are used to store data values in key:value pairs
# They are unordered, mutable(changeable) and don't allow duplicate keys

dir = {
    "Nmae": "Ankit singh",
    "Age" : 21,
    "usn" : "22btrcn026"
}

# Changing and adding the new element in the dictionary

dir["Phone no."] = 6204862703
dir["usn"] = "22btrcn25"
print(dir)

# nested dictionary

Student = {
    "Name" : "Rahul Singh",
    "Usn" : "22btrcn026",
    "Phone no." : 6204862703,
    "Marks" : {
        "CNS" : 49,
        "LA" : 39,
        "SSS" : 42,
        "DMND" : 46
    }
}

print(Student["Marks"]["CNS"])

# Dictionary Methods

#Students.keys() - Returns all the keys
print(Student.keys())

#Student.values() - Returns all values
print(Student.values())

#Students.items() - Returns all (key,val) pair
print(Student.items())

#Student.get("key") - Return the key according to values
print(Student.get("Name"))

#Student.update(newDict) - Insert the specific items to the dictionary
Student.update({"City" : "Mashrakh"})
print(Student)
# Adding multiple cites
newDir = {
    "Fee" : 275000,
    "Branch" : "CSE General",
    "Section" : "A"
}
Student.update(newDir)
print(Student)

# Practice problem

# Store following word meanings in a python dictionary:
# table: "a pice of furniture", "list of facts and figues"
# cat : "a small animal"

dictionary = {
    "table" : ["a pice of furniture" "," "list of facts and figues"],
    "cat" : "a small animal"
}
print(dictionary)

# you are given a list of subject for 1 students. Assum one classroom is required for subject.
# How many classrooms are needed by all students
# "python", "jave", "c++", "python", "javascript", "java", "python", "java", "c++", "c"

subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
no_of_classroom = len(subject)
print(no_of_classroom)

# WAP to enter marks of three subjects from the user and store them in a dictionart.
# Start with and empty dictionary and add one by one. Using subject name as key and marks as value.

marks = {}

a = int(input("Enter the maths marks: "))
marks.update({"Maths" : a})

b = int(input("Enter the science marks: "))
marks.update({"Science" : b})

c = int(input("Enter the Hindi marks: "))
marks.update({"Hindi" : c})

d = int(input("Enter the English marks: "))
marks.update({"English" : d})

e = int(input("Enter the Social Science marks: "))
marks.update({"Social Science" : e})

print(marks)
