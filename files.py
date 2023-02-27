#!/usr/bin/env python
# coding: utf-8

# ## Question 2a

# In[ ]:


import pandas as pd

import clean_up as cl


text = open("big_data.txt", "r")

# lifted from lecture
all_words = []
counter = 0
for line in text:
    words = line.split()
    counter = counter + 1
    # if counter == 20:
    #     break
    for word in words:
        word = cl.clean(word)
        all_words.append(word)
        
# convert into dataframe and use value_counts method
df_words = pd.DataFrame(data=all_words, columns=("words",))
df_counts = df_words["words"].value_counts()
print(len(df_counts))

print(df_counts)
print(df_counts.iloc[100:120])

df_counts.to_csv("wordcount.csv")


# ## Question 2b

# In[ ]:


import pandas as pd

import clean_up as cl



        
# number of words is the lenght of the list
print("Number of words:", len(all_words))

print("Number of words:", df_words["words"].count())


# ## Question 2c

# In[ ]:



        
# Loop over the words. Determine the length of each word and add up.
# The count could also been done in the first loop, but conveniet
# recycling
nchar = 0
# this could also be done using df_words
for word in all_words:
    nchar = nchar + len(word)
    
print("number of characters:", nchar)


# ## Question 2d

# In[ ]:


import pandas as pd

import clean_up as cl


all_letters = []
counter = 0
for word in all_words:
    word = cl.clean(word)
        
    # convert word into list of letters
    letters = list(word)
    # loop to append letters
    for l in letters:
        all_letters.append(l)
        
        
# convert into dataframe and use value_counts method
df_letters = pd.DataFrame(data=all_letters, columns=("letters",))
df_counts = df_letters["letters"].value_counts()

print(df_counts)
df_counts.to_csv("lettercount.csv")


# ## Question 2e

# In[ ]:


import pandas as pd

import clean_up as cl


length = 0

for word in all_words:
    # do not forget to clean up
    word = cl.clean(word)
    if len(word) > length:
       length = len(word)
       # stores the new longest word
       lword = word

# the sep keyword argument of print allows to replace the 
# space between values to be replace by other characters, 
# an empty string in this case. Spaces need to be added by hand,
# giving better control over the layout.
print("The longest word is ", lword, ". It has", length," characters.", sep="")


# In[ ]:




