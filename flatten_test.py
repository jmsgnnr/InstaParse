import json
# import pandas as pd

with open('message_1.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)


def func1(data):
    for key,value in data.items():
        print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            func1(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func1(val)
                    
new_date = func1(data)
