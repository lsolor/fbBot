import random
from pymessenger.bot import Bot
from flask import Flask, request
import json
from bot import Bot
app = Flask(__name__)
ACCESS_TOKEN = 'EAAFpjOT0M4sBAMqI3ZC2soJTSViVhIwFFt6XUSVCVWTABAKZCIg1gcdfPJC7xluARK9aRCnEapB1FUbZC7TKHKVCdYfF4qZAY4I6v9E3B5bH6xWYTFZCYdb1ecTSyxQtgolyMRVZBmHl7ZCbXGjQq3DhH3f59qHE5hdM61JyoYdJ32BLZB9iS7VG9vZCgBN6jglUZD'

VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

GREETINGS = ['hi', 'hello', 'howdy']
# app.route is a decorator that knows the below function
# @app is the name of the object containing the flask app
# app.route decorator takes the URL of a route, and HTTP methods
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == 'secret':
            return str(challenge)
        return '400'
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        return verify_fb_token(token_sent)
        # if the request was not get, it must be POST and we can just proceed with sending a message # back to user
    else:
        # json data we are looking at
        # {"object": "page", "entry": [{"id": "101210667972429", "time": 1571287751199, "messaging": [
        #     {"sender": {"id": "2438800666188023"}, "recipient": {"id": "101210667972429"}, "timestamp": 1571287693949,
        #      "message": {
        #          "mid": "d__TBKqfqSSKA-V0JlitX-nsTLSUzZqlhs1OlZllM4sm0fJa32U8KFq1KjbGyz0VppSfWavOT8Jdq0cn-utCOg",
        #          "text": "workedddd"}}]}]}
        #print(request.data)
        data = json.loads(request.data)
        messaging_event = data['entry'][0]['messaging']
        bot = Bot(ACCESS_TOKEN)

        for message in messaging_event:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            if text_input in GREETINGS:
                response_text = 'Hello. Welcome to my first bot!'
            else:
                response_text = 'I\'m still learning'
            print('Message from user ID {} - {}'.format(user_id, text_input))
            bot.send_text_message(user_id, response_text)
        return '200'
    # else:
    #     # get whatever message a user sent the bot
    #     output = request.get_json()
    #     for event in output['entry']:
    #         messaging = event['messaging']
    #         for message in messaging:
    #             if message.get('message'):
    #                 # Facebook Messenger ID for user so we know where to send response back to
    #                 recipient_id = message['sender']['id']
    #                 if message['message'].get('text'):
    #                     response_sent_text = get_message()
    #                     send_message(recipient_id, response_sent_text)
    #                 # if user sends us a GIF, photo,video, or any other non-text item
    #                 if message['message'].get('attachments'):
    #                     response_sent_nontext = get_message()
    #                     send_message(recipient_id, response_sent_nontext)
    # return "Message Processed"


# def verify_fb_token(token_sent):
#     # take token sent by facebook and verify it matches the verify token you sent
#     # if they match, allow the request, else return an error
#     if token_sent == VERIFY_TOKEN:
#         return request.args.get("hub.challenge")
#     return 'Invalid verification token'
#
#
# def send_message(recipient_id, response):
#     #sends user the text message provided via input response parameter
#     bot.send_text_message(recipient_id, response)
#     return "success"

if __name__ == '__main__':
    app.run(debug = True)
