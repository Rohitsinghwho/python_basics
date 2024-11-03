# Mutable and immutable are type of data types.
# In python we have to types of data type 
# ---mutable(which can be changed in place)
# ---immutable(Which cannot be changed instead there referece is changed upon reassigning)

# Mutable data types are list,dict,sets,array
# Immutable data types are int, float, string, boolean, tuple,bytes

# immutable example
name="Rohit" #this is a string data type which is immutable
print(id(name)) #this will print the memory location of the string "Rohit"
name="Rohan" #this will change the reference of the name variable
print(id(name)) #this will print the memory location of the string "Rohan"
# as no one is pointing to memory location where "Rohit" is stored so it will be automaticlly freed by the python garbage
# controller

score=5
print(id(score)) #this will print the memory location of integer "5"
newScore=score #i have assigned a new variable to score now it will also point to memory location of integer "5"
print(id(newScore))  #it will print the same memory location address
#now if i try to change the original score to 10 then will the newScore change? lets see.
score=15  #changed the score to 15
print(score) #printing score to check the theory
print(newScore) #printing newScore to check the theory 
#oh no it changed the main score variable but not the newScore amazing...

# lets try to print there memory locations
print(id(score))  #the memory loaction to the score variable changed to another address but the earlier address was already 
#stored inside the newScore
print(id(newScore))  #that is why it is still pointing to that address and printing the old value of score
# lets try to change the newScore to 20
newScore=20 #changing the newScore to 20
print(newScore) #printing newScore to check the theory
print(score) #printing score to check the theory
#now the same will happen to memory location pointing to '5' it will pointed by no one , as newScore will be now pointing to
# memory loaction "20". So the memory location of 5 will be freed by garbage collector



