from cgitb import text
from hashlib import new
import json
from this import d
from typing import final
from pandas.io.json import json_normalize
import pandas as pd

with open("message_1.json", 'r', encoding='utf-8') as json_data:
    content = json_data.read()
    clean = content.replace(r"[\"\',]`", '')
    data = json.loads(clean)

# print(data)


df1 = pd.DataFrame(data['messages'])
# print(df1)

df2 = pd.DataFrame.drop(df1, axis=1,columns=['sender_id_INTERNAL','is_unsent','is_taken_down','bumped_message_metadata','call_duration', 'audio_files','videos'])
# print(df2)

norm_df = pd.json_normalize(data['messages'], max_level=4)
# print(norm_df)

dropped_df =pd.DataFrame.drop(norm_df, axis=1,columns=['sender_id_INTERNAL','is_unsent','photos', 'is_taken_down','call_duration', 'audio_files','videos', 'bumped_message_metadata.bumped_message','share.profile_share_username','share.link','share.share_text', 'share.original_content_owner', 'share.profile_share_name','reactions','type', 'bumped_message_metadata.is_bumped'])
# print(dropped_df)

only_chat_df= dropped_df.dropna(subset = ['content'])
# print(only_chat_df)

drop_likes_df = only_chat_df[only_chat_df["content"].str.contains("Liked a message") == False]
drop_likes_df['timestamp_ms'] = pd.to_datetime(drop_likes_df['timestamp_ms'], unit='ms')
print(drop_likes_df)


#html output test

result_df = drop_likes_df.to_html()
text_file = open("ben.html" , "w", encoding='utf-8')
text_file.write(result_df)
text_file.close()