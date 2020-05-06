#!/usr/bin/env python
# coding: utf-8
ADITYA TIWARI
2K19CSUM01001
PART C
# In[1]:


#Q1.) What is the syntax to call a constructor of a base class from child class.
#A1.) To call a constructor of a base class from child class,:-
#   we call using super()Command.


# In[3]:


#Q2.) How is a class made as inherited class (syntax of child class).
#A2.) class Parent:
#   pass
#       class Child(Parent):
#           pass
#Child class inherit the Parent class.


# In[5]:


#q3.
#suppose we have two dictionary dic1 & dic2\n",
people = {1: {'name': 'aditya', 'age': '21', 'sex': 'Male'},
          2: {'name': 'marie', 'age': '23', 'sex': 'Female'}}
# then we can print particular element of a dictionary as:
print(people)


# In[ ]:


#Q1. :- Write a program that calculates and prints the value according to the formula given below.
#Take three values from user. Q= square root (( 2*value1*value2)/value3)

#ANS 1 :-
import math
def sqrroot (value1,value2,value3):
    Q=math.sqrt(( 2*value1*value2)/(value3))
    return Q

value1 =int(input("Enter value1 :- "))
value2 =int(input("Enter value2 :- "))
value3 =int(input("Enter value3 :- "))

sqrroot = sqrroot (value1,value2,value3)

print ("Q = ", sqrroot)


# In[ ]:


#Q2. Please write a program which accepts a string from console and print the characters that have even indexes.
#ANS 2 :-
print("Please enter text to print::")
inputchars = input()

if inputchars:
    string = ""
    for i in inputchars:
        if inputchars.index(i) % 2 == 0:
            string += str(i)

print('-----ADITYA--TIWARI-----')
print("You Entered:", inputchars)
print("Result:")
print(string)


# In[ ]:





# 
