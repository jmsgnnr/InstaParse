import json
from pandas import json_normalize
import pandas as pd

with open('message_11.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)


try:
    chat_df = pd.DataFrame(data['messages'])
    # we will add more columns here as we flatten json data

    chat_df = chat_df.filter(['sender_name','timestamp_ms','content'])

    
    # grab nested share/reactions
    # chat_df['react'] = chat_df['reactions'].fillna('[]').apply(lambda x: [d['reaction'] for d in x])

    # drops non chat messages
    chat_df = chat_df.dropna(subset=['content'])

    # only returns chat messages, drops 'liked a message'
    chat_df = chat_df[chat_df["content"].str.contains("Liked a message") == False]

    # user may need to change unit type, test data is in Mountain Standard Time
    chat_df['timestamp_ms'] = pd.to_datetime(chat_df['timestamp_ms'], unit='ms')

    #html output needs latin-1 to parse extra chars in ig download
    chat_df_html = chat_df.to_html()

    with open("html_output.html" , "w", encoding='LATIN-1') as f:
        f.write(chat_df_html)
except Exception as e:
    print(e)


print(chat_df)



