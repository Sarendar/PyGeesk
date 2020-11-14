import os
import configparser
import time

#----------------------------------------------
# Counting_pairs() is function has with option parameter
# Return counting pairs from list
#------------------------------------------------
def Counting_pairs(options):
    list_values = options['input_list'].split(',')
    # converting string values to integer in list
    list_values =list( map(int ,list_values))
    diff = int(options['k'])
    print("Given Input List is: {} with difference {} ".format(list_values,diff))
    
    # retrn pairs if difference is 0 or otherwise else
    if diff == 0:
        ret_val = {(x,(x+diff)) for x in list_values if list_values.count(x) > 1}
    else:
        ret_val = {(i,(i+diff)) for i in list_values if (i+diff) in list_values}
        
    print("Counting pair values are: {}, for the difference: {} \nAnd number of pairs is: {}".format(ret_val,diff,len(ret_val)))

if __name__ == "__main__":
    print("Counting pair initiated....!")
    strt_time = time.time()
    config_obj = configparser.ConfigParser()
    ### Reading config file and getting values from section
    config_obj.read(os.path.join("config.ini"))
    config_values = config_obj["Counting_Pairs"]
    #print("Configuration Object....!",config_values)
    
    #calling  function
    Counting_pairs(config_values)
    print(" *** Time taken for the execution in seconds: {}  ***".format(time.time() - strt_time))