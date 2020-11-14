#!/usr/bin/env python
# coding: utf-8

# In[67]:


import os
import time
#import pandas as pd
from itertools import combinations
from collections import defaultdict


# In[69]:


strt_time = time.time()
# data = [
# ("username1","phone_number1", "email1"),
# ("usernameX","phone_number1", "emailX"),
# ("usernameZ","phone_numberZ", "email1Z"),
# ("usernameY","phone_numberY", "emailX"),
# ]

data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
("usernameA","phone_number1", "emailB"),
("usernameB","phone_numberB", "emailBX"),
("usernameC","phone_numberA", "emailZ1"),
]

#------------------------------------------------
# GenerateIndices class contain with consructor and matchedIndices method
# we are initializing data veriable throhg clss object
#------------------------------------------------
class GenerateIndices():
    def __init__(self,data):
        self.input_data = data
        
    #--------------------------------------------------
    # Method with only have self parameter  
    # It return the mached indices sublist and non mached indices sublist as in singlelist
    #--------------------------------------------------
    def matchedIndices(self):
        print("mached indices script initiated..... And Object! ",self)
        print("Input data............ ",self.input_data)
        pairs_data = dict()
        pairs_data= defaultdict(list)
        # iterating data list to get subsets and indexes from it
        for id_index, sub_set in enumerate(self.input_data):
            #iterating subset and append to dictonaly along with keys
            for i in sub_set:
                pairs_data[i].append(id_index)

        matched_indexes = []
        not_matched_indexes = []
        print("Pairs data object as dictonary.....! ",pairs_data)
        # Iterating dictonary of pairs data to get key values
        for key,val in pairs_data.items():
            #print("Key Value: ",key,val)
            # if val of length > 1 , extend list with values 
            if len(val) > 1:
                matched_indexes.extend(val)
            else:
                not_matched_indexes.extend(val)

        # make unique indexes of not_matched_indexes and matched_indexes
        matched_indexes = set(matched_indexes)
        not_matched_indexes = set(not_matched_indexes)
        not_matched_indexes = not_matched_indexes.difference(matched_indexes)

        #print ("mached aand not machhed indexes: ",matched_indexes,not_matched_indexes)
        #print("Intersection values............",list(not_matched_indexes))
        print(" \n***************************** \n Mached inidces sublit: {} \n Not mached indices sublist: {}".format(list(matched_indexes),list(not_matched_indexes)))
        print(" Expected Return list: {} \n*****************************".format([list(matched_indexes),list(not_matched_indexes)]))
        
        print(" \n \n *** Time taken for the execution in seconds: {}  ***".format(time.time() - strt_time))

# Class object creat on and passing data as parameter
# And calling object method
indices_object = GenerateIndices(data)
indices_object.matchedIndices()



# In[ ]:




