# Sets is the collection of the unordered itemes.
# Each elements in the set must be unique and immutable
# Set is mutable but their elements are immutable

collection = {2,8,"Ankit","Kumar", 5,1,10}
print(type(collection))
print(collection)

# creating empty sets
newCollection = set()
print(type(newCollection))

# Function in Sets

# 1. sets.collection(el) - to add the element in the set
newCollection.add("Sony")
print(newCollection)
newCollection.add((5,10,15,20,85))
print(newCollection)

# 2. sets.remove(el) - to remove element from the set
newCollection.remove("Sony")
print(collection)

# 3. sets.clear() - empty the set by deleating all the elements
collection.clear()
print(collection)

collection.add("Ankit")
collection.add("Singh")
collection.add("22BTRCN026")
print(collection)

# 4. sets.pop() - to removes a random value 
# collection.pop()
# print(collection)

# 5. sets.union(set2) - combines both set values and returns new
collection.union(newCollection)
print(collection)

collection.remove("Ankit")

# 6. sets.intersection(set2) - combine common values and returns new
set1 = {1,2,3,4}
set2 = {1,2,5,6}
set3 = set1.intersection(set2)
print(set3)

