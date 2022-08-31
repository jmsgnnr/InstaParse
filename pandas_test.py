from calendar import c
from cgitb import text
from hashlib import new
import json
from this import d
from typing import final
from pandas.io.json import json_normalize
import pandas as pd

with open("message_1.json", 'w', encoding='UTF-8') as json_data:
    content = json_data.read()
    # clean = content.replace(r"[\"\',]`", '')
    data = json.loads(content)

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
print(df4)

#html output test

result_df = df4.to_html()
text_file = open("html_test.html" , "w", encoding='ascii')
text_file.write(result_df)
text_file.close()



# normalized json test
# norm_df = pd.json_normalize(data['messages']['reactions'],max_level=4)
# print(norm_df)

# dropped_df =pd.DataFrame.drop(norm_df, axis=1,columns=['sender_id_INTERNAL','is_unsent','photos', 'is_taken_down','call_duration', 'videos', 'bumped_message_metadata.bumped_message','share.profile_share_username','share.link','share.share_text', 'share.original_content_owner', 'share.profile_share_name','reactions','type', 'bumped_message_metadata.is_bumped'])
# print(dropped_df)

# only_chat_df= dropped_df.dropna(subset = ['content'])
# print(only_chat_df)




