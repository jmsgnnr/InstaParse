## User Story 

###### A user wants to download their message history from instagram and view their messages with a friend. Utilizing the python script in this repository, a user can parse their downloaded json data and create an .html file with their chat history with another user of their choosing.

### Steps:
1. ``` git clone ``` this repository

2. from your code editor terminal ```py pip install requirements.txt ```
(Requirements)
```json
distlib==0.3.4
Jinja2==3.1.2
numpy==1.22.3
pandas==1.4.2
spark==0.2.1
Unidecode==1.3.4
```
3. navigate to ->messages inside your downloaded instagram .json file
4. add your json file as message_1.json 
5. ```py python pandas_test.py ```
6. To view your html output, we have downloaded the visual studio code extension 'live-server' and used command Alt+L to view our html output. 
