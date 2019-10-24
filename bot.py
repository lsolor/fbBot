import requests
import json

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v4.0/me/'

class Bot(object):

    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    def send_text_message(self, psid, message, messaging_type="RESPONSE"):
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'messaging_type': messaging_type,
            'recipient': {'id': psid},
            'message': {'text': message}
        }

        params = {'access_token': self.access_token}
        self.api_url = self.api_url + 'messages'

        response = requests.post(self.api_url,
                                 headers= headers, params = params,
                                 data=json.dumps(data))
        print(response.content)

#bot = Bot('EAAFpjOT0M4sBAMqI3ZC2soJTSViVhIwFFt6XUSVCVWTABAKZCIg1gcdfPJC7xluARK9aRCnEapB1FUbZC7TKHKVCdYfF4qZAY4I6v9E3B5bH6xWYTFZCYdb1ecTSyxQtgolyMRVZBmHl7ZCbXGjQq3DhH3f59qHE5hdM61JyoYdJ32BLZB9iS7VG9vZCgBN6jglUZD')
#bot.send_text_message(2438800666188023,'testing 123')
   #     curl - X
    #     POST - H
    #     "Content-Type: application/json" - d
    #     '{
    #     "messaging_type": "<MESSAGING_TYPE>",
    #     "recipient": {
    #         "id": "<PSID>"
    #     },
    #     "message": {
    #         "text": "hello, world!"
    #     }
    #
    # }' "https://graph.facebook.com/v4.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"