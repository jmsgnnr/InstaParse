import json
import pandas as pd

with open('message_1.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

df1 = pd.DataFrame(data['messages'])
# we will add more columns here as we flatten json data
df1 = df1.filter(['sender_name','timestamp_ms','content'])
# drop blank content vals
df1 = df1.dropna(subset=['content'])
# only returns chat messages, drops 'liked a message'
df1 = df1[df1["content"].str.contains("Liked a message") == False]
# user may need to change unit type, test data is in Mountain Standard Time
df1['timestamp_ms'] = pd.to_datetime(df1['timestamp_ms'], unit='ms')

#html output needs latin-1 to parse extra chars in ig download
df1_html = df1.to_html()
text_file = open("html_test.html" , "w", encoding='LATIN-1')
text_file.write(df1_html)
text_file.close()




