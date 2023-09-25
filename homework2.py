#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence 
#on a single line.


# In[95]:


numList = []
for i in range(2000,3201):
    if (i%7==0 and i%5!=0):
        numList.append(i)
print(*numList, sep = ',')
        


# In[ ]:


#Question 2: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# In[86]:


def fact_fun(a):
    fact = 1
    if a>1:
        fact = a*fact_fun(a-1)
    return fact

num = int(input())
if num >= 0:
    print(fact_fun(num))
    


# In[ ]:


#Question 3: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that 
#is an integral number between 1 and n (both included). and then the program should print the dictionary. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()


# In[32]:


squares = {}
target = int(input())
for i in range(1, target+1):
    squares[i] = i*i
print (squares)


# In[ ]:


#Question 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
#and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple


# In[39]:


input_list = input().split(',')
print(input_list)
print(tuple(input_list))


# In[ ]:


# Question 5: Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.
#Hints: Use init method to construct some parameters


# In[57]:


class StringFormat:
    def __init__(self):
        self.name = input()
        self.length = len(self.name)
    def getString():
        self.name = input()
        
    def printString(self):
        print("Upper Case: "+str.upper(self.name))
        print("Length: "+str(self.length))

person = StringFormat()
person.printString()
            


# In[ ]:


#Question 6: Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H:
#C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.
#Example: Let us assume the following comma separated input sequence is given to the program:
#100,150,180 The output of the program should be: 18,22,24
#Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
#(for example, if the output received is 26.0, it should be printed as 26)
#In case of input data being supplied to the question, it should be assumed to be a console input.


# In[96]:


import math
def printEquation(D):
    C = 50
    H = 30
    Q = math.sqrt((2 * C * D)/H)
    return Q

inputList = input().split(',')
outputList = []
for eachNum in inputList:
    outputList.append(round(printEquation(int(eachNum))))
    
print(*outputList,sep=',')
    


# In[72]:


#Question 7: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,.., Y-1.
#Example: Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


# In[78]:


inputStr = input().split(',')
X = int(inputStr[0])
Y = int(inputStr[1])
newArray=[]
for i in range(X):
    newArray.append([])
    for j in range(Y):
        newArray[i].append(i*j)
print(newArray)


# In[79]:


#Question 8: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program: without,hello,bag,world
#Then, the output should be: bag,hello,without,world
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# In[98]:


inputList = input().split(',')
print(*sorted(inputList), sep = ',')


# In[99]:


#Question 9: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be: HELLO WORLD
#PRACTICE MAKES PERFECT
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# In[108]:


outputStrings = []
while True:
    inputStrings = input()
    if inputStrings:
        outputStrings.append(str.upper(inputStrings))
    else:
        break
print(*outputStrings, sep = '\n')


# In[109]:


#Question 10: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
#We use set container to remove duplicated data automatically and then use sorted() to sort the data.


# In[113]:


inputStringList = input().strip().split(' ')
print(*sorted(set(inputStringList)))


# In[ ]:


#Question 11: Define a class, which have a class parameter and have a same instance parameter.

#Hints: Define a instance parameter, need add it in init method
#You can init a object with construct parameter or set the value later


# In[119]:


class studentProfile:
    major = 'Automotive'
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def printStudentDetails(self):
        print("Name: "+self.name)
        print("ID: "+self.id)
john = studentProfile('John Smith','123')
john.printStudentDetails()


# In[120]:


#Question 12: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and 
#the values are square of keys. The function should just print the values only.
#Hints: Use dict[key]=value pattern to put entry into a dictionary.
#Use ** operator to get power of a number.
#Use range() for loops.
#Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


# In[129]:


def dict_gen():
    dictOne = {}
    for i in range(1,21):
        dictOne[i] = i**2
    for key,value in dictOne.items():
        print(value)
dict_gen()


# In[128]:


#Question 13: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

#Hints: Use dict[key]=value pattern to put entry into a dictionary.
#Use ** operator to get power of a number.
#Use range() for loops.
#Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


# In[130]:


def dict_gen():
    dictOne = {}
    for i in range(1,21):
        dictOne[i] = i**2
    for key,value in dictOne.items():
        print(key)
dict_gen()


# In[131]:


#Question 14: Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
#Hints: Use ** operator to get power of a number.
#Use range() for loops.
#Use list.append() to add values into a list.


# In[134]:


squaresList = []
for num in range(1,21):
    squaresList.append(num**2)
print(squaresList)


# In[135]:


#Question 15: Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

#Hints: Use "for" to iterate the tuple
#Use tuple() to generate a tuple from a list.


# In[136]:


evenList = []
for itr in (1,2,3,4,5,6,7,8,9,10):
    if(itr%2==0):
        evenList.append(itr)
evenTuple = tuple(evenList)
print(evenTuple)


# In[137]:


#Question 16: Define a class named American and its subclass NewYorker.

#Hints: Use class Subclass(ParentClass) to define a subclass.


# In[138]:


class American:
    name = "John Smith"
class NewYorker(American):
    city = "New York"
newPerson = NewYorker()
print(newPerson.city)


# In[139]:


#Question 17: Define a class named Rectangle which can be constructed by a length and width.
#The Rectangle class has a method which can compute the area.

#Hints: Use def methodName(self) to define a method.


# In[141]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculateArea(self):
        self.area = self.length*self.width
        return self.area
shapeOne = Rectangle(5,4)
print(shapeOne.calculateArea())


# In[142]:


#Question 18: Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
#Hints: To override a method in super class, we can define a method with the same name in the super class.


# In[145]:


class Shape:
    area = 0
    def printArea(self):
        print(area)
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def printArea(self):
        area = self.length**2
        print(area)
newShape = Square(2)
newShape.printArea()


# In[146]:


#Question 19: Write a function to compute 5/0 and use try/except to catch the exceptions.

#Hints: Use try/except to catch exceptions.


# In[148]:


def divZero():
    try:
        i = 5/0
    except:
        print("Illegal Operation")
divZero()


# In[ ]:


#Question 20: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

#Hints: Use set() to store a number of values without duplicate.


# In[151]:


oldList = [12,24,35,24,88,120,155,88,120,155]
newSet = set(oldList)
newList = list(newSet)
print(newSet)


# In[ ]:




