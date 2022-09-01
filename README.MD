## User Story 

###### A user wants to download their message history from instagram and view their messages with a friend. Utilizing the python script in this repository, a user can parse their downloaded json data and create an .html file with their chat history with another user of their choosing. For version 1, we excluded shares and reactions... keeping it simple and only returning our text history.

### Steps:
1. ``` git clone ``` this repository

2. from your code editor terminal ```pip install requirements.txt```
```json
distlib==0.3.4
Jinja2==3.1.2
numpy==1.22.3
pandas==1.4.2
spark==0.2.1
Unidecode==1.3.4
```
3. navigate to -> messages -> inbox -> '@username' inside your downloaded instagram zip folder. Each user you've chatted with should have a different folder attached to their name.
4. add your message history file from your selected convo as message_1.json
5. run ```py python pandas_test.py ``` in the terminal once your file is added.
6. To view your html output, we have downloaded the visual studio code extension 'live-server' and used command Alt+L in our html_output.html file to view our chat history!
