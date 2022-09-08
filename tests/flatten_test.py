import json
import pandas as pd

with open('../message_11.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)


def parse_data(data):
    #  any time we have a function that calls itself, we need a base case! 
    if data == None: 
        return
    for key,value in data.items():
        print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            parse_data(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) != type(str()) or type(val) != type(list()):
                    parse_data(val)
                    




