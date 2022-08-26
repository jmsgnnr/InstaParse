from cgitb import text
from hashlib import new
import json
from this import d
from typing import final
from unittest import result
from pandas.io.json import json_normalize
import pandas as pd
import re
import datetime as dt

with open('message_1.json') as json_data:
    data = json.load(json_data)

df1= pd.DataFrame(data['messages'])

df2 = pd.DataFrame.drop(df1, axis=1,columns=['sender_id_INTERNAL','is_unsent','is_taken_down','bumped_message_metadata','call_duration', 'audio_files','videos'])

# df2['reactions'] = [','.join(map(str, l)) for l in df2['reactions']]
# df2["content"] = df2['content'] + df2['reactions']

norm_df = pd.json_normalize(data['messages'], max_level=4)

dropped_df =pd.DataFrame.drop(norm_df, axis=1,columns=['sender_id_INTERNAL','is_unsent','photos', 'is_taken_down','call_duration', 'audio_files','videos', 'bumped_message_metadata.bumped_message','share.profile_share_username','share.link','share.share_text', 'share.original_content_owner', 'share.profile_share_name','reactions','type', 'bumped_message_metadata.is_bumped'])

only_chat_df= dropped_df.dropna(subset = ['content'])

drop_likes_df = only_chat_df[only_chat_df["content"].str.contains("Liked a message") == False]

# special chars test 1 

# drop_likes_df['content'] = drop_likes_df['content'].str.replace(r"[\"\',]", '')

# special chars test 2

# drop_likes_df['content']= drop_likes_df['content'].apply(lambda val: unicodedata.normalize('NFKD', val).encode('ascii', 'ignore').decode())

drop_likes_df['timestamp_ms'] = pd.to_datetime(drop_likes_df['timestamp_ms'], unit='ms')

drop_likes_df['content'] = drop_likes_df['content'].map(lambda x: re.sub(r'[^\w\s]', '', x))

print(drop_likes_df)

#html output test

result_df = drop_likes_df.to_html()
text_file = open("index.html" , "w", encoding='utf-8')
text_file.write(result_df)
text_file.close()