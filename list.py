# In python we can store multiple data type in the a single list.
# In python the string is immutable and list is mutable(we can change it)

nums = [10,15,16,80,90]

# len(nums) - give he length of the list
print(len(nums))

# Slicing in list
print(nums[2:4]) # 4th index is not included.

#list.append(2) - to add in the list at the last
nums.append(1)
print(nums)

# list.sort() - used to sort the list in ascending order
nums.sort()
print(nums)

# list.sort(reverse = true) - to sort the list in descending order
nums.sort(reverse = True)
print(nums)

# list.reverse() - it will reverse the list like 0 index become last and last become 0th
nums.reverse()
print(nums)

#list.insert(idx, el) - to insert the element at the specific position
nums.insert(5, 8)
nums.sort()
print(nums)

# list.remove() - remove the first occurrence of the element
print(nums)
nums.remove(8)
print(nums)
# list.pop(idx) - remove the element at the paticular index
print(nums)
nums.pop(5)
print(nums)
