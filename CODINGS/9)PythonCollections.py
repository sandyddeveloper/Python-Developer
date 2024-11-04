#List
a = [1,2,3,4,5]
print(type(a))
print(dir(a))
print(a)
a.append(7)
a.append(8)
a.append("sandy")
a.append(True)
a.append(4)
print(a)

# if i want to add the data in first
a.insert(0,11)# zero is position and value to insert is 11 

#  if i want to modify the data or update the data
a[0]= 11
print(a)

# if i want to remove a data 
a.pop(4)
print(a)

a.pop() # its only remove last element 

# combining two list into single list 
a = [11,24,20]
b = [4,8,6]
a.extend(b)
print(b)



