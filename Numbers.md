# Python Number

 - Never do the operations like noob programer
 - x+y*z (wrong)
 - (x+y)*z (correct)
 - if we print(x,y,z) it will return a tuple (1,2,3)
 - if we want to find power use (**) operator
 - power can store a very long number almost infinite
 - we can use ** operator with negative number

 #### precisions
    result=1.1/3.0
    print(result)
    output will be -> 0.333333333
    We can set the precision in python

#### Diff between repr ,str, print

- They are way to output the value
- repr( ) is used for debugging, evaluation, it outputs often with quotes and escapes
- str( ) is used to output human-readable form, it represents in the form of string ofter more concise
- print( ) used to display to the console.

#### ex
    a="Chai"
    print(a)
    print(str(a))
    print(repr(a))

#####
    Chai
    Chai
    'Chai'

### Comparisons in python
    x=2
    y=3
    z=4
    if(x<y<z):
        print(true)
    else:
        print(false)

- In python (x<y<z) is same as (x<y and y<z)
- (1==2<3) it will output false as it is same as (1==2 and 2<3) 
- This is a short hand for python
- It is not a industry practice though  


#### floor, ceil, trunc

- floor gives us the bottom value always for ex - 3.9 the output will be 3.

- ceil gives us the upper value always for ex -3.1 the output will be 4.

- trunc takes the number toward zero always for ex - 3.9 ouput will be 3. -2.8 the ouput will be -2.


#### Python can handle complex numbers
    a=3+4j
    print(a*2) output -> 6+8j


#### Python can handle octal values
    a=0o10
    print(a) output -> 8
    --Method of finding octal values
    x=oct(64)
    print(x) -> 0o100
#### Python can handle hexadecimal values
    a=0xFF
    print(a) output -> 255
    --Method of finding hex values
    x=hex(64)
    print(x) ->0x40
#### Python can handle binary values
    a=0b1000
    print(a) output -> 8
    --method of finding binary values
    x=bin(64)
    print(x)

#### other methods of finding hex, binary and octal
    x=int('64',8)  //for octal value
    print(x) ->output 52 

    y= int('64',16) //for hex
    pirnt(y) -> output 100

    z= int('1000',2) //for binary
    print(z) -> output 16


#### Decimals are handled nicely in python 
- with the help of Decimal();
- import decimal from Decimal 
- Decimal('0.1')

    
#### SETS  are also numbers in python

##### you can find union, internsections etc here
    a={1,2,3,4,5}
    b={1,3,5}
    print(a&b)  //intersection
    print(a|b)  //union
    print(a-b)  //diff
    print(a^b)  //xor
    print(a-a);
    print(type({}))  //output -> <class 'dict'>

####
    {1, 3, 5}
    {1, 2, 3, 4, 5}
    {2, 4}
    {2, 4}
    set( )  //it does not give { } becuase it is type of dict
    <class 'dict'>

