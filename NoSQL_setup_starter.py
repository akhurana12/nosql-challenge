#!/usr/bin/env python
# coding: utf-8

# # Eat Safe, Love

# ## Part 1: Database and Jupyter Notebook Set Up

# In[1]:


#Import the data provided in the `establishments.json` file from your Terminal. Name the database `uk_food` and the collection `establishments`.

#Within this markdown cell, copy the line of text you used to import the data from your Terminal. This way, future analysts will be able to repeat your process.

#e.g.: Import the dataset with mongoimport --type json -d uk_food -c establishments --drop --jsonArray establishments.json


# In[2]:


# Import dependencies
from pymongo import MongoClient
from pprint import pprint


# In[3]:


# Create an instance of MongoClient
mongo = MongoClient(port=27017)


# In[4]:


# confirm that our new database was created
mongo.list_database_names()


# In[5]:


# assign the uk_food database to a variable name
db = mongo['uk_food']


# In[6]:


# review the collections in our new database
db.list_collection_names()


# In[7]:


# review a document in the establishments collection
db.establishments.find_one()


# In[8]:


# assign the collection to a variable
establishments = db['establishments']


# ## Part 2: Update the Database

# 1. An exciting new halal restaurant just opened in Greenwich, but hasn't been rated yet. The magazine has asked you to include it in your analysis. Add the following restaurant "Penang Flavours" to the database.

# In[9]:


# Create a dictionary for the new restaurant data
new_restaurant = {
    "BusinessName":"Penang Flavours",
    "BusinessType":"Restaurant/Cafe/Canteen",
    "BusinessTypeID":"",
    "AddressLine1":"Penang Flavours",
    "AddressLine2":"146A Plumstead Rd",
    "AddressLine3":"London",
    "AddressLine4":"",
    "PostCode":"SE18 7DY",
    "Phone":"",
    "LocalAuthorityCode":"511",
    "LocalAuthorityName":"Greenwich",
    "LocalAuthorityWebSite":"http://www.royalgreenwich.gov.uk",
    "LocalAuthorityEmailAddress":"health@royalgreenwich.gov.uk",
    "scores":{
        "Hygiene":"",
        "Structural":"",
        "ConfidenceInManagement":""
    },
    "SchemeType":"FHRS",
    "geocode":{
        "longitude":"0.08384000",
        "latitude":"51.49014200"
    },
    "RightToReply":"",
    "Distance":4623.9723280747176,
    "NewRatingPending":True
}


# In[10]:


# Insert the new restaurant into the collection
establishments.insert_one(new_restaurant)


# In[11]:


# Check that the new restaurant was inserted
establishments.find_one({"BusinessName": "Penang Flavours"})


# 2. Find the BusinessTypeID for "Restaurant/Cafe/Canteen" and return only the `BusinessTypeID` and `BusinessType` fields.

# In[12]:


# Find the BusinessTypeID for "Restaurant/Cafe/Canteen" and return only the BusinessTypeID and BusinessType fields
query = {"BusinessType":"Restaurant/Cafe/Canteen"}

fields = {
    "BusinessTypeID": 1,
    "BusinessType":1
}


# In[13]:


establishments.find_one(query,fields)


# 3. Update the new restaurant with the `BusinessTypeID` you found.

# In[14]:


# Update the new restaurant with the correct BusinessTypeID
establishments.update_one(
    {"BusinessName": "Penang Flavours"},
    {
        "$set":
            {"BusinessTypeID":1}
    }
)


# In[15]:


# Confirm that the new restaurant was updated
establishments.find_one({"BusinessName": "Penang Flavours"})


# 4. The magazine is not interested in any establishments in Dover, so check how many documents contain the Dover Local Authority. Then, remove any establishments within the Dover Local Authority from the database, and check the number of documents to ensure they were deleted.

# In[16]:


# Find how many documents have LocalAuthorityName as "Dover"
count = establishments.count_documents({'LocalAuthorityName': 'Dover'})
count


# In[17]:


# Delete all documents where LocalAuthorityName is "Dover"
establishments.delete_many({'LocalAuthorityName': 'Dover'})


# In[18]:


# Check if any remaining documents include Dover
count = establishments.count_documents({'LocalAuthorityName': 'Dover'})
count


# In[19]:


# Check that other documents remain with 'find_one'
establishments.find_one()


# 5. Some of the number values are stored as strings, when they should be stored as numbers.

# Use `update_many` to convert `latitude` and `longitude` to decimal numbers.

# In[20]:


# Change the data type from String to Decimal for longitude and latitude
establishments.update_many(
    {},
    [
        {
            '$set':
            {
                'geocode.latitude':{'$toDouble': '$geocode.latitude'},
                'geocode.longitude': {'$toDouble': '$geocode.longitude'}
            }
        }
    ]
)


# Use `update_many` to convert `RatingValue` to integer numbers.

# In[21]:


# Set non 1-5 Rating Values to Null
non_ratings = ["AwaitingInspection", "Awaiting Inspection", "AwaitingPublication", "Pass", "Exempt"]
establishments.update_many({"RatingValue": {"$in": non_ratings}}, [ {'$set':{ "RatingValue" : None}} ])


# In[22]:


# Change the data type from String to Integer for RatingValue
establishments.update_many(
        {'_id': ['_id']},
        {'$set':  {'$toDouble': "$Rating Value"}},
    )


# In[23]:


# Check that the coordinates and rating value are now numbers


# In[ ]:




