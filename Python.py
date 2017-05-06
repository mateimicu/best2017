
# coding: utf-8

# # https://github.com/micumatei/best2017
# ---
# # Applications for Python
# 
# #### Web and Internet Development
#  - Django
#  - Flask
#  - Pyramid
#  
# #### Scientific and Numeric
#  - SciPy 
#  - Pandas 
# 
# #### Machine learning
#  - Tensorflow
#  - scikit-learn
#  
# #### Clound and DevOps
#  - Openstack
#  - Fabric 
#  - Ansible
# 
# 
# https://github.com/vinta/awesome-python
# 
# Online python shells:
#  - https://www.python.org/shell/
# 
# MSI windows:
#  https://www.python.org/downloads/release/python-2713/
#  sau
#  http://192.168.2.9:8080/
# 

# In[1]:

"""
Python Basics
"""


# In[2]:

# Comentarii

"""
Comentariu pe mai multe linii.
"""


# In[3]:

# Print functons/keyword 

print "Hello World"


# In[4]:

# Type of something
print type("Hello World")


# In[5]:

# Tipuri de date

# Int
some_int = 10
print "some_int:      ", type(some_int)
# Float
some_float = 10.5
another_float = .10 # == 0.10
print "some_float:    ", type(some_float)
print "another_float: ", type(another_float)



# Boolean
bool_true = True
bool_false = False

print "bool_true:     ", type(bool_true)
print "bool_false:    ", type(bool_false)

# String
some_string = "Hello!"
print "some_string:   ",type(some_string)



# In[6]:

# Boolean Operators

print True and False
print True or False



# In[7]:

# Comparison operators

print  "1 < 2      ", 1 < 2
print  "2 <= 2     ", 2 <= 2
print  "2 >= 2     ", 2 >= 2
print  "2 >= 2     ", 2 >= 2
print  "3 != 2     ", 3 != 2
print  "3 is 4     ", 3 is 4
print  "3 is not 4 ", 3 is not 4 


# In[8]:

# (Py2.7) Mathematical operators
print "1 + 1  ", 1 + 1
print "2 - 1  ", 2 - 1
print "5 / 2  ", 5 / 2
print "5 // 2  ", 5 // 2
print "5 % 2  ", 5 % 2
print "float(5) / float(2)  ", float(5) / float(2)
print "float(5) // float(2)  ", float(5) // float(2)
print "float(5.5) / float(2)  ", float(5.5) / float(2)
print "float(5.5) // float(2)  ", float(5.5) // float(2)


# In[9]:

# Liste
lista = [1, 2, 3, 4, 5]


# Lucru cu listele
print "Primul elemente: ", lista[0]
print "Primul-ish elemente: ", lista[-5]
print ""
print "Ultimul elemente: ", lista[4]
print "Ultimul-ish elemente: ", lista[-1]
print ""

print ""
print ""

# Slicing
print "lista[incepit:sfarsit:pas]"
print "lista[0:4]   ",lista[0:4]
print "lista[0:-1]  ",lista[0:-1]
print "lista[2:]    ",lista[2:]
print "lista[:2]    ",lista[:2]
print ""
print "lista[0:4:2] ",lista[0:4:2]
print "lista[0:4:3] ",lista[0:4:3]
print "lista[0:4:-1]",lista[0:4:-1]
print "lista[4:0:-1]",lista[4:0:-1]
print "lista[::-1]",lista[::-1]

print "Add new items \n\n"
print "Lista", lista
lista.append(10)
print "Lista", lista
lista[2] = "new item"
print "Lista", lista


# In[10]:

# Lista complexa
lista_complexa = [
    ["a", "b", "c"],
    ["a", 1, 2.0],
    [
        ["lista"],
        ["in"],
        ["lista"]
    ]
]

print "Primul randc    ",lista_complexa[0]
print "Al treilea rand ",lista_complexa[2]
print "Nested lists    ",lista_complexa[2][1]


# In[11]:

# Tuple
some_tuple = (1, 2, "aaa")
print "All items :", some_tuple
print "Slice :", some_tuple[1:]


# In[12]:

# Dictionare Hash Tables

some_dict = {
    "key1": "value1",
    "key2": "value2"
}

print "Val1  ", some_dict["key1"]
print "Val1  ", some_dict["key2"]

# Usefull functions
print "Kyes: ", some_dict.keys()
print "Values: ", some_dict.values()
print "Items: ", some_dict.items()


# In[13]:

# If-elif-else
a = 12
if a == 1:
    print "<a> este == 1"
elif a == 2:
    print "<a> este == 2"
elif a == 3:
    print "<a> este == 3"
else:
    print "Else"


# In[14]:

# For-1
print "Primele 10 numere"
for item in range(10):
    print item


# In[15]:

# For-2
print "Primele 10 numere incepand de la 1 "
for item in range(1, 11):
    print item


# In[16]:

# For-3
print "Iterarea unei liste"
some_list = ["first", "second", 3]
for item in some_list:
    print "--", item


# In[17]:

# While
itr = 0
while itr < 20:
    if itr % 2 == 0:
        print itr
    itr += 1


# In[18]:

# Builtin functions Help
help(str)


# In[19]:

# Builtin functions dir
dir(str)


# In[20]:

# Builtin functions 
dir(__builtins__)


# In[21]:

## Definirea de functii
def my_func(param1, param2):
    print "Param1", param1
    print "Param1", param1
    return param1 + param2


# In[22]:

my_func(1, 2)


# In[23]:

my_func("aa", "bb")


# In[24]:

# Modules
import math
print "Pi :", math.pi


# In[25]:

# Ce avem in modul ?
dir(math)


# In[26]:

# Descrierea modulelor 
help(math)


# In[27]:

# More functions
# clasic fibonacci
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# In[28]:

fib(10)

