#!/usr/bin/env python
# coding: utf-8

# In[64]:


#Q1:

dict={}
print(dict)


# In[14]:


#Q2:

a={"A":"10","B":"20"}
print(a)


# In[18]:


#Q3:Create a dictionary with different data types for keys

student={
1:"A",
2:"B",
3:"C",
}
print(student)


# In[63]:


#Q4:Print all the items of a dictionary

dict={
"A":1,
"B":2,
"C":3,

}
print(dict.items())


# In[62]:


#Q5:5Delete an element of a dictionary

dict={
"A":1,
"B":2,
"C":3,
}
print(dict)
del dict['B']
print(dict)


# In[31]:


#Q.6:Delete full dictionary

dict={
"A":1,
"B":2,
"C":3,
}
print("Dict. is")
print(dict)
print("Deleting Dict.")
del dict
print("full disc. deleted")


# In[61]:


#Q7:Print value for a key

dict={
"A":1,
"B":2,
"C":3,
}
for key,value in dict.items():
    print(key,value)


# In[67]:


#Q8:To check if a key id is present in a dictionary

dict={
"A":"1",
"B":"2",
}
if "A" in dict:
    print("VALUE EXIST")
else:
    print("VALUE DOES NOT EXIST")


# In[66]:


#Q9:9Update a value of a key

dict={
"A":1,
"B":2,
"C":3,
}
print(dict)
dict['A']=7
print(dict)


# In[68]:


#Q10:Add a new key value pair

dict={
"A":1,
"B":2,
"C":3,
}
print(dict)
dict['F']=8
print(dict)


# In[72]:


#Q11:Print Dictionary keys{1,10} and values as square of keys

a={}
for i in range(1,10):
    a[i]=i**2
    print(a)


# In[75]:


#Q12:Print nested dictionary
dict={
"A":100,
1:"B",
5:{"A":200,
2:"C"},
"D":300,
}
print("\nNested dictionary")
print(dict)


# In[81]:


#Q13:Concatenate three dictionaries

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
d4={}
for  d in (d1,d2,d3):
    d4.update(d)
    print(d4)


# In[106]:


#Q14:Sum all the values of a dictionary

dict={
"A":1,
"B":2,
"C":3,
}
i=0
for key,value in dict.items():
    i=value+i
    print(i)


# In[105]:


#Q15:Accessing an element of a nested dictionary
# Nested dictionary having same keys

Dict = { "Dict1": {"name": "A", "age": "19"},
         "Dict2": {"name": "B", "age": "25"}}
  
# Prints value corresponding to key &#39;name&#39; in Dict1
print(Dict['Dict1']['name'])
  
# Prints value corresponding to key &#39;age&#39; in Dict2
print(Dict['Dict2']['age'])


# In[97]:


#Q16:Write python script to print a dictionary where the keys are numbers between 1 and 15 and the
#values are square of the keys.

dict={}
for key  in range(1,16):
    dict[key]=key*key
    print(dict)


# In[104]:


#Q17:Insert factorial of keys in values and print dictionary
    
dict={}
factorial = 1
for key in range(1,4):
    factorial=factorial*key
    dict[key]=factorial
    print(dict)


# In[ ]:




