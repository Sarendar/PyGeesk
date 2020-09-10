import os
import pandas as pd
import configparser

'''
#How to read config values from config.ini file
'''
if __name__ == "__main__":

    print("entered in to main function....")
    config_obj = configparser.ConfigParser()
    path = os.path.join("config.ini")
    config_obj.read(path)

    config_years = config_obj['Years']
    print("Years.............",config_years["config_years"])
    config_inst = config_obj["Inst"]
    print("Inst..........",config_inst["instrument"],config_inst["es"])




