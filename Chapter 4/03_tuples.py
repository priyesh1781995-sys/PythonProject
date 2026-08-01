a = (1,2,5,6)    # Tuple with more than one elements
print(type(a))

a = (1,)         # This is a tuple with one element
print(type(a))

a = (1,45,346,3424,False,"Rohan","Shivam")   # This is also a tuple with different data types
print(type(a))

a = (1,45,346,3424,False,"Rohan","Shivam")   # This will give error because we can't change tuple. 
a[0] = 453

a = (1,45,346,3424,False,"Rohan","Shivam")   # This will give error
print(a)
print(type(a))



