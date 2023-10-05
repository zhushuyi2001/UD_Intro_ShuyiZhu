#!/usr/bin/env python
# coding: utf-8

# # Exercise 00
# Write a piece of code that allocates a list of 20 integers and initializes each element by its index multiplied by 5. Print the result.

# In[1]:


integer_list = []

for i in range(20):
    integer_list.append(i * 5)

print(integer_list)


# # Exercise 01
# Define a function that takes an integer as input, prints  all integers that it is divisable by, and returns the largest one.

# In[6]:


def find_divisors_and_return_largest(n):
    divisors = [] 

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            print(i, end=' ')

    if len(divisors) > 0:
        return max(divisors)
    else:
        return None


# # Exercise 02
# - create a dictionary with 6 keys and values of your choice
# - write a function that takes a dictionary and a value as input and returns whether the value occurs as a key in the dictionary
# - write a function that takes a dictionary as input, and returns the dictionary but the keys are swapped with their values (resolve the issue if a value occurs twice!)

# In[ ]:


my_dict = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange",
    "blueberry": "blue",
    "kiwi": "green"
}


# In[7]:


def check_value_in_dict(input_dict, value):
    return value in input_dict.keys()


# In[9]:


def swap_keys_and_values(input_dict):
    swapped_dict = {}
    for key, value in input_dict.items():
        if value not in swapped_dict:
            swapped_dict[value] = key
        else:
            if isinstance(swapped_dict[value], list):
                swapped_dict[value].append(key)
            else:
                swapped_dict[value] = [swapped_dict[value], key]
    return swapped_dict


# # Exercise 03
# Define a function that creates a dictionary of the first n fibonacci numbers as values paired with their indices as keys. 

# In[10]:


def fibonacci_dictionary(n):
    fib_dict = {}
    a, b = 0, 1

    for i in range(n):
        fib_dict[i] = a
        a, b = b, a + b

    return fib_dict


# In[12]:





# In[ ]:




