# Python Strings



##Declaration
- A string in Python is declared by enclosing a sequence of characters in quotes.
- A="rohit"

### Types of String
- "str" , 'str', ""str""
- Raw String: r"str"

#### Accessing the Sting

- s="abc"
- print(s[0]) # prints a
- ch=s[o]
- print(ch)

##### String Slicing

-  For example a string s="Rohit Singh"
-  Now we want to slice it and print only Rohit.

###

    s="Rohit Singh"
    len= len(s)
    print(s[0:5]) # first Method
    print(s[:5])  #Second Method
    print(s[:-5]) #third method

- Ouput of following code
###
    Rohit 
    Rohit
    Rohit

- As we can see that we sliced the string using [:] notation.
- During Slicing an string or list we can mention three parameters 1: starting index, 2: end index (not inclusive), 3: hop(jump)
- If we don't mention the start index it will start from the beginning of the string.
- If we don't mention the end index it will go till the end of the string.
- If we don't mention the hop it will take 1 as default value.


##### String Split

- For example we have a string 
- s= "Lemon, ginger, masala"
- Now we want to split it into a list of words.
###
    s="Lemon, ginger, masala"
    print(s.split(", ")) # prints ['Lemon', ' ginger', ' masala']

- split takes a argument that on which bases to divide the string. basically a seprator.


#### String placeholders

- if we want to inject variables inside the string dynamically.
- for example we have
###
    chai_type="Masala chai"
    quantity=2
    order="I ordered {} cups of {}"
    order = order.format(quantity, chai_type)
    print(order)
###
    I ordered 2 cups of Masala chai

- Here we use {} empty curly braces in the string and then after that use the method .format(arg) to specifiy the variables. 
- Order is important. 


#### Conversion of list to string

    cha=["Lemon", "Ginger", "Masala"]
    newstr= "-".join(cha)
    print(newstr)

####
    Lemon-Ginger-Masala

- we can use " ".join(arg) to convert to string. 
- first " " takes the seprator.
- second it takes the list.
