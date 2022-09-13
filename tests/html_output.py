import os
import json
import codecs
import sys
import textwrap
from unidecode import unidecode
import pandas as pd

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
file_handle = codecs.open("message_1.json", "r", "utf-8")
str_data = file_handle.read()
file_handle.close()
my_jobj = json.loads(str_data)

f = codecs.open('out.html', 'w+', "utf-8")
f.write("Your messages are as follows <br>");
f.write("__________________________________________________<br><br>")

# Latest message will be first! So displaying in the reverse order.
for i in range (len(my_jobj["messages"]) - 1, -1, -1) :
    df_tmp = []
    sender_name = my_jobj["messages"][i]["sender_name"]
    ts = my_jobj['messages'][i]['timestamp_ms']
    try:
        text = my_jobj["messages"][i]["content"]
        rslt =  textwrap.fill(sender_name + ": "  +  text.translate(non_bmp_map), 50)
        df_tmp.append(text)

        for char in text:
            char.encode("ascii")

    except:
        try:
            share_text = my_jobj["messages"][i]["share"]["share_text"]
            link = my_jobj["messages"][i]["share"]["link"]
            rslt  = textwrap.fill(sender_name + ":   <img src='"+ link +"'>" + share_text.translate(non_bmp_map), 50 ) 
        except:
            # reactions= my_jobj["messages"][i]["reactions"]
            rslt  = sender_name + ": " + 'fix'

    f.write(rslt)
    f.write("<br><br>")
    # print(rslt)
f.write("<br><br>__________________________________________________<br>")
f.write("\tScript completed execution!<br><br>");
f.close()