import os
import datetime

class MemCache():

    def __init__(self):

        ''' Constructor of MemCache class '''
        self.cache = {}
        self.max_cache_size = 5
        #print("\nEntereddddd..................! class")

    def __contains__(self,key):
        ''' Returns True or False depending on whether or not the key is in the
        cache '''
        print("\n Present values in cache ...........",[cache_val for cache_val in self.cache])
        return key in self.cache

    @property
    def Size(self):
        """Return the size of the cache """
        return len(self.cache)

    def update(self,key,value):
        ''' Update the cache dictionary and optionally remove the oldest item'''
        now = datetime.datetime.now()
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            # deleting oldest record if condition met
            self.delete_oldest()

        self.cache[key] = {'date_access': now.strftime("%d/%m/%Y %H:%M:%S"),'random_val':value}

    def delete_oldest(self):
        ''' Remove the entry that has the oldest accessed date '''
        print(" \n Oldest record going to delete ............")
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_access'] < self.cache[oldest_entry]['date_access']:
                oldest_entry = key
        self.cache.pop(oldest_entry)
        print(" \n Deleted oldest record is: ", oldest_entry)