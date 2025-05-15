# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values

mylist =[0,1, "two", 3.2, False]
# print(len(mylist))
# print(mylist[2])
# print(mylist[-1])
# mylist[0]=10
# print(mylist)

# to access a member of a sequence type, use []
#a string is also a list. ach character in a string is indexed. however, you cant change the char value or a string.
mystr ="I am unbwogable"
# print(mystr[0])
#print(mystr)
# add a list to another list
mylist2 =[2,4,5,6,7]

#print(mylist + mylist2)

# use slices to get parts of a sequence
#print(mylist2[::2])

# you can use slices to reverse a sequence
#print(mylist2[-1:-4:-1])

# Tuples are like lists, but they are immutable () -hold data thta is not going to change
mytuple = (1,2,3,4,5, "hey")
#print(mytuple [2])
#mytuple[2]=5
#print(mytuple)# brings error because tuple are immutable.

# Sets are also sequences, but they contain unique values{}- enforce uniqueness in their membership.
myset ={3,2,5,7,2, "hello"}
#print(myset) #excludes printing the last 2, because it only allows one unique value (no duplication) 

# Set, however, can not be indexed like lists or tuples

# print(myset[0]) # this will cause an error

# Test for membership  -- use 'in' to check if a value exists in a sequence
print(3 in mylist2)
print(4 in mylist2)
print (7 in myset)