#!/usr/bin/env python
# coding: utf-8

# In[33]:


#Q6)the value of bacon= 22 and Bacon+1 will be?
Bacon = 22
Bacon+1
#it should be Bacon = Bacon +1
print(Bacon)


# In[12]:


#Q2) Difference between variable and String? 

#Ans) Variable: Variable use to store value 

#String: String is a datatype use to store string value 
B= 'Bacon'
print(B)
# B is a variable
#'Bacon' is a datatype string


# In[30]:


#Q3)Describe three different data types.
#1) Numeric: int, float, complex number
a = 1
print(type(a))
b = 1.20
print(type(b))
c =  2 + 2j
print (type(c))
#2) Boolen : Yes, No
x= True
print(type(x))
y= False
print(type(y))
#3)Sequence type: String, List,tupple
S= 'Hello world' 
print(type(S))
L = ['2','4','6','8']
print(type(L))                   
T= (3,7,9,11,13)
print(type(T))                 #the only difference(tupple vs list) is of brackets for tuples we use parenthesis


# In[32]:


#Q4)What is an expression made up of? What do all expressions do?
#Expression is a combination of mathematical operators, variables, and values.
#When we command python to print, the interpreter evaluates the expression and displays the results. 
a = 23 # statement
a = a  + 23 # expression
print(a)


# In[ ]:


#Q1)In the below elements which of them are values or an expression? eg:- values can be
#integer or string and expressions will be mathematical operators.
*,-,+,/= these all are expressions
'hello' = string value
-87.8   = float value
6= int value


# In[6]:


#the value of 'spam'+'spamspam'
s='spam'+'spamspam'
print(s)


# In[ ]:


#Q8)  Why is eggs a valid variable name while 100 is invalid?
# eggs is a valid variable name we can give some value to store and later can recognize what it is
# whereas 100 cannot be storable and it cannot  begin with numbers
#variable name should be in form of letters only


# In[8]:


#Q7) the value of'spam*3'
s= 'spam'*3
print(s)


# In[ ]:


#Q9)What three functions can be used to get the integer, floating-point number, or string
#version of a value?
# for int = int()
# for float = float()
# for string = string()


# In[10]:


#Q10)'I have eaten' + 99 +'burritos'
# This will show an error TypeError: can only concatenate str (not "int") to str
#to solve this we need to convert int to str


# In[11]:


'I have eaten'+'99'+'burritos'


# In[ ]:




