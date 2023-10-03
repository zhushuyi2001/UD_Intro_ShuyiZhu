#!/usr/bin/env python
# coding: utf-8

# # Exercise 00
# Write a bit of code that prints _Introduction to Programming_ to the console and execute the cell

# In[70]:


print("Introduction to Programming")


# -----------------------------------------------------------------------------
# # Exercise 01
# Hello World is traditionally the first program anyone writes. It is
# very simple and the only thing it should do is print Hello World! to the
# terminal window.
# Create a file called HelloWorld.py and edit the contents so it prints Hello World! to the terminal and execute it using the command line.

# -----------------------------------------------------------------------------
# # Exercise 02
# Write some code to print your name, email, and age on separate lines. For each element first assign it to a variable and use the variable to print. 
# 
# Bonus: try to create the print statement for all variable in one line of code. (hint: '\n' is the character for a new line)

# In[5]:


name = "Shuyi Zhu"
email = "ucbvhuc@ucl.ac.uk"
age = 22 

print("Name:", name)
print("Email:", email)
print("Age:", age)

print("Name: {Shuyi Zhu}\nEmail: {ucbvhuc@ucl.ac.uk}\nAge: {22}")





# -----------------------------------------------------------------------------
# # Exercise 03
# Print the numbers 0, 178, -21, 2938 divided by 49, 436 multiplied with 9948 and 12 to the power of 20
# 
# (Hint: Look up the documentation of basic arithmetic operators)

# In[6]:


result1 = 0 / 49
result2 = 178 / 49
result3 = -21 / 49
result4 = 2938 / 49
result5 = 436 * 9948
result6 = 12 ** 20

print("0 divided by 49 is:", result1)
print("178 divided by 49 is:", result2)
print("-21 divided by 49 is:", result3)
print("2938 divided by 49 is:", result4)
print("436 multiplied by 9948 is:", result5)
print("12 to the power of 20 is:", result6)


# -----------------------------------------------------------------------------
# # Exercise 04
# Print sin(200), cos(100), tan($\pi$/4)
# 
# (Hint: Look up for how to use trigonometric function, and how to get the value of $\pi$.)

# In[21]:


import math

sin_200=math.sin(math.radians(200))
cos_100=math.cos(math.radians(100))
tan_π_4=math.tan(math.radians(math.pi/4))

print("cos100=",cos_100)
print("sin200=",sin_200)
print("tanπ/4=",tan_π_4)


# -----------------------------------------------------------------------------
# # Exercise 05
# Write a program to read your first and last names from the console seperately, and then print them on the console together, separated by a space.

# In[47]:


first_name = "Shuyi"
last_name="Zhu"
full_name=first_name+" "+last_name
print(full_name)


# -----------------------------------------------------------------------------
# # Exercise 06
# Write a program that determines whether a number given as user input is positive or negative
#  
# You will need to convert the console input from a string to a number first!

# In[57]:


user_input = input("Enter a number: ")

number = float(user_input)
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# -----------------------------------------------------------------------------
# # Exercise 07
# Write a program that picks a random number between 1-20 and makes the user guess until they get the number right. Then print a congratulations message
# - (Find out yourself how to generate a random integer)
# - Bonus: make the user choose the range within which they have to guess
# - Bonus: keep track of how many guesses were made and print this at the end

# In[60]:


import random


# In[ ]:





# -----------------------------------------------------------------------------
# # Exercise 08
# Ask a sentence as input, then print the words in alphabetical order.
# Hint: look up how to split up a string

# In[61]:


sentence = input("Enter a sentence: ")
words = sentence.split()
sorted_words = sorted(words)

print("Words in alphabetical order:")
for word in sorted_words:
    print(word)


# -----------------------------------------------------------------------------
# # Exercise 09
# Write a program using for loops to print a christmas tree of x lines high
# specified by the user.
# (use for loops)
# so for instance, a chrismas tree of 4 high should looks like this:
# 
# ```
# 
#     *
#    ***
#   *****
#  *******
#     |
# 
# ```
# 
# hint: first combine strings into a variable before printing

# In[77]:


height = int(input("Enter the height of the Christmas tree: "))

for i in range(1, height + 1):
        print(" ", end="")
for k in range(2 * i - 1):
        print("*", end="")
for i in range(height):
    print(" ", end="")

print("|")


# -----------------------------------------------------------------------------
# # Exercise 10
# Write a piece of code that prints the first $n$ numbers of the padovan sequence

# In[ ]:


none

