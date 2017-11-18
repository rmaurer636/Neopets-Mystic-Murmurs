
# coding: utf-8

# ### Neopets Mystic Murmuers Nov 2017

# In[106]:

import csv


# We open each textfile in my folder with the csv.reader() function, then we save each list into three different lists in python for analysis.

# In[115]:

tex1, text2, text3 = [], [], []

with open('text1.txt') as inputfile:
    text1 = list(csv.reader(inputfile, delimiter=' '))
    text1 = text1[0]
with open('text2.txt') as inputfile:
    text2 = list(csv.reader(inputfile, delimiter=' '))
    text2 = text2[0]
with open('text3.txt') as inputfile:
    text3 = list(csv.reader(inputfile, delimiter=' '))
    text3 = text3[0]


# One we have our lists, lets analyze list 1 with list 2 and get the common characters at the same index. Then we do the same with list 1 and list 3.

# In[116]:

joined_text1 = []
joined_text2 = []

for i in range(len(text1)):
    if text1[i] == text2[i]:
        joined_text1.append(text1[i])
for i in range(len(text1)):
    if text1[i] == text3[i]:
        joined_text2.append(text3[i])


# Once we have our joined lists, I perform an "and" operation which only joins if the two inputs are the same. EX: a and b = 0, a and a = a

# In[117]:

print joined_text1, joined_text2

result = joined_text1 and joined_text2
print ''.join(result)

