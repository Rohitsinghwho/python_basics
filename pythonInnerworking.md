# Python inner working

- As we know that python stores the data in memory and assign the referece to the variable.
## if we create a variable say,

- a=5 
- Now inside the memory the refererce on memory location 5 is stored inside variable a.
- Now if we reassign b=5.
- Then python internally optimizes the performance and assign the same memory loation 5 to variable b.
- Now python internally has a way to count refereces toa memory location via a variable called as ref_count which is stored in the memory.
-It is a very troublesome process to access this ref_count variable as it is the thing of python which is not avaible to users.
- But we can use the sys module to get the ref_count of a variable.
- sys.getrefcount(a) will return the ref_count of variable a.
- The ref_count of a variable is decremented when the variable is reassigned or deleted.
- The ref_count of a variable is incremented when the variable is assigned to another variable.
- The ref_count of a variable is incremented when the variable is passed to a function.

## Are there No Datatypes in python?
- Python does not have a data type that are assigned to the variable. 
- Python is dynamically typed language which means that the data type of a variable is determined at runtime.
- Python does not have a data type that is assigned to the variable at compile time.
- Python assignes the datatype to a value in the memory location that you are of this and that type.


## Why does the memory location in python keeps on changing in case of strings
      import sys
      username="nobo"

      print(id(username))

        NewUser="nobo";

        print(id(NewUser))

        print(sys.getrefcount("nobo"))

### The ouput changes at every new execution,
    PS D:\Python> python -u "d:\Python\python_inner.py"
    2436207318224
    2436207318224
    5
    PS D:\Python> python -u "d:\Python\python_inner.py"
    2257723954384
    2257723954384
    5
    PS D:\Python> python -u "d:\Python\python_inner.py"
    1945576510672
    1945576511776
    3
    PS D:\Python> python -u "d:\Python\python_inner.py"
    2019641627856
    2019641627856
    5

### why is that?
- This is because of python's internal optimizations, or we can say python's string interning behaviour.
- Before assigning the memory location to a variable python checks for the common strings , if the common string is present within the intern pool. python assignes the reference of that memory to the new variable.if not then it create a reference.(In case of string.)
- As for the continous change in the memory location python sometime does not use intern pool and creates a new reference to memory leading to the changing memory location. That is why ref count is greater than 2.

#### String Interning pool.
-   It is a mechanism to optimize memory management.it stores only one copy of each unique strings in memory.When we create a string literal in our code python first checks if the string is in the intern pool if it exists it assignes the same ref to the variable if not then it stores the copy in the intern pool and then assignes.

#### If we perform operations of a number of other types then will python create new objects in the memory based on the operation?
#### lets perform a operation on the number.
    a=10
    print(id(a))
    b=5;
    print(id(b))
    a= a + b;

    print(a);
    print(id(a));
    print(id(b));

#### The ouptut will be:-
    PS D:\Python> python -u "d:\Python\python_inner.py"
    140731850746584
    140731850746424
    15
    140731850746744
    140731850746424
    PS D:\Python> 

- As we can see that the memory location of a was previously "140731850746584" and after performing the operation on a python reassignes a diffrent memory location to a that had value 15 stored in it.
- So it proves that python does change the referneces based on the operations.

### Does python actually stores the refernce and assigne then again for optimization and not create diffrent objects in the memory?

    mylist=[1,2,3]
    print(id(mylist))
    mylisttwo= mylist;
    print(id(mylist));
    mylist=[3,4,5]
    mylist=[1,2,3]
    print(id(mylist))

#### now refer this code and think will the variable mylist at last be pointing to same location as mylisttwo?
    1390396772928
    1390396772928
    1390397076928

- The memory location where [1,2,3] was stored earlier it was something. Then we assigned location [1,2,3] to my list two.
- After that we changed the the memory location of mylist to [2,3,4]. so now it might be pointing to this memory location.
- Now [1,2,3] is still in the memory assigned to mylisttwo. 
- Then i again assigned [1,2,3] to mylist. it amazingly it produced the same refernce.

#### Now with the help of same example lets try to take it other wAY.
    mylist=[1,2,3]
    print(mylist)
    mylisttwo= mylist;
    print(mylisttwo)
    mylist[0]=22
    print(mylist)
    print(mylisttwo)

#### now the output is :-
    [1, 2, 3]
    [1, 2, 3]
    [22, 2, 3]
    [22, 2, 3]

- It printed the same values as of mylist why ? 
- Because intially we assigned a memory location which was storing [1,2,3] to mylist.
- Then we assgined mylisttwo to mylist which internally assinged the same memory location to mylisttwo.
- Now mylisttwo is also pointing where mylist is pointing.
- And if we change mylist it will also change mylisttwo beacuse of same memory location.
- And because of mutable type.

### Now lets take one more example
    l1= [1,2,3]
    l2=[1,2,3]
    print(id(l1))
    print(id(l2))
    l1[0]=5
    print(l1)
    print(l2)

#### Just think what will be the internal behaviour here ?
    2921130037824
    2921130082496
    [5, 2, 3]
    [1, 2, 3]

- As we stored the same values inside two variable that was [1,2,3].
- But python did not assign them the same memory refernce.
- And when we changed the value in one list it did not change the value in other
- Becuase they were not pointing to the same memory location.


## The creating of a new objects in the memory and not creating is totally based on the types of data ..whether it is immutable or mutable.
-   If the data is immutable. The if we try to give same value to two diffrent variable they will obvisoly point to the same memory location.
- If the data is mutable. Then in some cases it may be given other address in the memory.
- The cases may be that we are assigned a memory location of one variable to other.


