# Mutable and immutable are type of data types.
# In python we have to types of data type 
# ---mutable(which can be changed in place)
# ---immutable(Which cannot be changed instead there referece is changed upon reassigning)

# Mutable data types are list,dict,sets,array
# Immutable data types are int, float, string, boolean, tuple,bytes

# ........................immutable example.........................................................
name="Rohit" #this is a string data type which is immutable
# print(id(name)) #this will print the memory location of the string "Rohit"
name="Rohan" #this will change the reference of the name variable
# print(id(name)) #this will print the memory location of the string "Rohan"
# as no one is pointing to memory location where "Rohit" is stored so it will be automaticlly freed by the python garbage
# controller

score=5
# print(id(score)) #this will print the memory location of integer "5"
newScore=score #i have assigned a new variable to score now it will also point to memory location of integer "5"
# print(id(newScore))  #it will print the same memory location address
#now if i try to change the original score to 10 then will the newScore change? lets see.
score=15  #changed the score to 15
# print(score) #printing score to check the theory
# print(newScore) #printing newScore to check the theory 
#oh no it changed the main score variable but not the newScore amazing...

# lets try to print there memory locations
# print(id(score))  #the memory loaction to the score variable changed to another address but the earlier address was already 
#stored inside the newScore
# print(id(newScore))  #that is why it is still pointing to that address and printing the old value of score
# lets try to change the newScore to 20
newScore=20 #changing the newScore to 20
#print(newScore) #printing newScore to check the theory
# print(score) #printing score to check the theory
#now the same will happen to memory location pointing to '5' it will pointed by no one , as newScore will be now pointing to
# memory loaction "20". So the memory location of 5 will be freed by garbage collector

#........Tuples..............

myTup= (1,2,3)  #way to define a tuple
# print(myTup)  #print the tuple
# print(myTup[0]) #accessing the element is same as list. Negative indexing is also same as list

# print(myTup[-1]) #accessing the element from behind is same as list
#lets try to change the value of the tuple
# myTup[0]= 10 #this will give an error because tuples are immutable and it will throw error on this particular line itself
#error ->  TypeError: 'tuple' obje ct does not support item assignment
# print(myTup) #this will not print the new value because tuples are immutable
# print(id(myTup)) #the address of the tuple will not change even if we try to change the value inside
#it because tuples are immutable

# ..............................mutable...............................................

#lets define some list and see
myLists= [101,'shaktimaan',3.14]  #way of defining a list
# print(myLists)  #printing the list
# print(id(myLists))  #printing the memory location
# print(myLists[1])  #way to access individual element from the list. Indexing starts from 0 in list and goes till length
#there is of more way of accessing it
# print(myLists[-2]) #it will print the same element but from behind. That is in negative indexing index starts from -1 to-len
#the last value is denoted as -1 index and so on.
#can we change the elements in the list? lets seee..
myLists[-2]= "Gajni"  #we changed the value of 1st index to Gajni.
# print(myLists[-2]) #it changed wooh.. it printed new value and now what about the previous value which was there
#at index -2? lets see
# print(myLists) #it changed the value at index -2 to Gajni from shaktimaan
#does the address of myList also changes after changing the value inside it? lets see..
# print(id(myLists)) #no the address is still the same that means the values are changed in the main address and they are mutable

#...............sets................

myset={1,2,3,4}
# print(myset) #printing the set
# print(id(myset)) #printing the memory location of the set
# print(myset[0]) #sets are also mutable and they are unordered collection of unique elements
# print(myset[-1]) #sets are unordered collection of unique elements
# these two print statements will throw error as sets are not indexed they are unordered
#lets try to change the value of the set
# myset.add(5) #adding a new element to the set
# myset[0]=9 #we cannot do that 
#error message -> TypeError: 'set' object does not support item assignment
# print(myset) #printing the set after adding the new element
# print(id(myset)) #printing the memory location of the set after adding the new element


# ..................Dictionary..................


#alias for dictionary is dict
mydict= {'one':'Iron Man','Two':'Thor',3:'Shasha'}  #way to declaring a dictionary
# print(mydict); #way of printing a dict
# print(id(mydict)); #printing the memory location of the dict
# print(mydict[0]) #dict are not accessed by these indexes. In dict we have the authority to change the
# index for our items
# that is if i try to do this it will print because i have the given the key 3 to it that is the index
print(mydict[3])
# print(mydict['one']) #way of accessing individual element from the dict. Indexing starts from
# 0 in list and goes till length there is of more way of accessing it
# if i try to change the value on a key will it work ? lets see
mydict[3]='Gray' #assiging index 3 to gray
# print(mydict)  #nice it changed the value on that key 




