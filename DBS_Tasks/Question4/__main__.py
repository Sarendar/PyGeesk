import os
import argparse
from mem_cache import MemCache as MC
import random
import time

if __name__ == "__main__":
    print("Memory cache script is initiated.....! \n ")

    # Parsing arguments through command line
    opt = argparse.ArgumentParser("Memory Cache")
    opt.add_argument("inputArg", type=str, help="First Input argument")
    opt.add_argument("-m", "--mode", choices=["info", "warn", "error"],default="info", help="Set run mode as either info warn or error")
    args = opt.parse_args()

    # List of values
    keys = ['test', 'red', 'fox', 'fence', 'junk',
            'other', 'alpha', 'bravo', 'cal', 'devo',
            'ele']
    s = args.inputArg
    #calling class object
    cache = MC()
    print(" \n Maximum size of the cache is : ", cache.max_cache_size)
    for i,key in enumerate(keys):
        print("\n \n ***************** \n Script sleep for 2 seconds in iteration {} ****".format(i+1))
        time.sleep(2)
        if key in cache:
            #print("Value exist in cache.......")
            continue
        else:
            # Generating random string using command line argument string
            # we treated this is new sting value going to store in cache
            value = ''.join([random.choice(s) for i in range(2)])
            cache.update(key,value)
            print(" \n New random string Value...........: ",value)
        print(" \n #%s iterations \n Present cache size: %s \n Present cached entries are: %s " % (i + 1,cache.Size,cache.cache))
