from cgitb import text
from hashlib import new
import json
from this import d
from typing import final
from pandas.io.json import json_normalize
import pandas as pd

# with open("message_1.json", 'r', encoding='utf-8') as json_data:
#     content = json_data.read()
#     clean = content.replace(r"[\"\'`'\;\",]`", '')
#     data = json.loads(clean)


with open('message_1.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)
# print(data)


df1 = pd.DataFrame(data['messages'])
# print(df1)
df2 = pd.DataFrame.drop(df1, axis=1,columns=['sender_id_INTERNAL','is_unsent','is_taken_down','bumped_message_metadata','call_duration', 'videos', 'type', 'photos', 'share', 'reactions'])
# print(df2)
df3 = df2.dropna(subset= ['content'])
# print(df3)

# only returns chat messages, drops 'liked a message'
df4 = df3[df3["content"].str.contains("Liked a message") == False]
df4['timestamp_ms'] = pd.to_datetime(df4['timestamp_ms'], unit='ms')
# print(df4)
print(df4)

#html output needs
result_df = df4.to_html()
text_file = open("html_test.html" , "w", encoding='LATIN-1')
text_file.write(result_df)
text_file.close()




