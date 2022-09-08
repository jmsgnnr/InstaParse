import json
from lib2to3.pgen2.pgen import DFAState
import pandas as pd

with open('message_11.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

test_data = pd.DataFrame(data['messages'])  

try:
    chat_df = pd.DataFrame(data['messages'])
    # we will add more columns here as we flatten json data

    chat_df = chat_df.filter(['sender_name','timestamp_ms','content','reactions','share'])

    # grab nested share/reactions 
    # chat_df['reaction'] =  pd.Series()
    # for index, row in chat_df.iterrows():
        
    #     if type(row['reactions']) == type(list()):
    #         reaction = (row['reactions'][0]['reaction'])
    #         print(type(reaction))
    #         row['reaction'] = reaction
         # if 'share' in chat_df:
    #     chat_df['share_text'] = chat_df['share']['share_text']
    #     chat_df['link'] = chat_df['share']['link']
    
    # drops non chat messages
    # chat_df = chat_df.dropna(subset=['content'])

    # only returns chat messages, drops 'liked a message'
    # chat_df = chat_df[chat_df["content"].str.contains("Liked a message") == False]

    # user may need to change unit type, test data is in Mountain Standard Time

    chat_df['timestamp_ms'] = pd.to_datetime(chat_df['timestamp_ms'], unit='ms')

    # print(chat_df.dropna(subset=['reaction']))

    #html output needs latin-1 to parse extra chars in ig download
    chat_df_html = chat_df.to_html()

    with open("html_output.html" , "w", encoding='LATIN-1') as f:
        f.write(chat_df_html)
except Exception as e:
    print(e)
 



