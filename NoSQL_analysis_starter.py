#!/usr/bin/env python
# coding: utf-8

# # Eat Safe, Love

# ## Notebook Set Up

# In[1]:


# Import dependencies
from pymongo import MongoClient
from pprint import pprint


# In[2]:


# Create an instance of MongoClient
mongo = MongoClient(port=27017)


# In[3]:


# assign the uk_food database to a variable name
db = mongo['uk_food']


# In[4]:


# review the collections in our database
mongo.list_database_names()


# In[5]:


# assign the collection to a variable
establishments = db['establishments']


# ## Part 3: Exploratory Analysis
# Unless otherwise stated, for each question: 
# * Use `count_documents` to display the number of documents contained in the result.
# * Display the first document in the results using `pprint`.
# * Convert the result to a Pandas DataFrame, print the number of rows in the DataFrame, and display the first 10 rows.

# ### 1. Which establishments have a hygiene score equal to 20?

# In[11]:


# Find the establishments with a hygiene score of 20
query = {'scores.Hygiene': 20}

# Use count_documents to display the number of documents in the result
print(f" Number of documents in result: {establishments.count_documents(query)}")


# Display the first document in the results using pprint
results = establishments.find(query)


pprint(results[0])


# In[14]:


import pandas as pd


# In[17]:


# Convert the result to a Pandas DataFrame
query = {'scores.Hygiene': 20}
results = establishments.find(query)

hygiene20 = pd.DataFrame(results) 

# Display the number of rows in the DataFrame
print(f"Rows in DataFrame: {len(hygiene20)}")

# Display the first 10 rows of the DataFrame
hygiene20.head(10)


# ### 2. Which establishments in London have a `RatingValue` greater than or equal to 4?

# In[26]:


# Find the establishments with London as the Local Authority and has a RatingValue greater than or equal to 4.
query ={'LocalAuthorityName': 'London', 'RatingValue': {'$gte': 4}}

# Use count_documents to display the number of documents in the result
num_documents = establishments.count_documents(query)
print(f"Number of establishments in London with RatingValue >= 4: {num_documents}")


# Display the first document in the results using pprint
if num_documents > 0:
    pprint(result[0]) 


# In[31]:


# Convert the result to a Pandas DataFrame
query = {'LocalAuthorityName': {'$regex': 'London'}, 'RatingValue': {'$gte': '4' }}
results = establishments.find(query)
LondonRatings = pd.DataFrame(results)

# Display the number of rows in the DataFrame
print(f"Rows in DataFrame: {len(LondonRatings)}")

# Display the first 10 rows of the DataFrame
LondonRatings.head(10)


# ### 3. What are the top 5 establishments with a `RatingValue` rating value of 5, sorted by lowest hygiene score, nearest to the new restaurant added, "Penang Flavours"?

# In[ ]:


# Search within 0.01 degree on either side of the latitude and longitude.
# Rating value must equal 5
# Sort by hygiene score

degree_search = 0.01
latitude = 
longitude = 

query = 
sort =  

# Print the results


# In[ ]:


# Convert result to Pandas DataFrame


# ### 4. How many establishments in each Local Authority area have a hygiene score of 0?

# In[ ]:


# Create a pipeline that: 
# 1. Matches establishments with a hygiene score of 0
# 2. Groups the matches by Local Authority
# 3. Sorts the matches from highest to lowest

# Print the number of documents in the result

# Print the first 10 results


# In[ ]:


# Convert the result to a Pandas DataFrame

# Display the number of rows in the DataFrame

# Display the first 10 rows of the DataFrame

