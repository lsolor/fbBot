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

        data = json.loads(request.data)
        messaging_event = data['entry'][0]['messaging']
        bot = Bot(ACCESS_TOKEN)

        for message in messaging_event:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            if text_input in GREETINGS:
                response_text = get_response();
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
def get_response():
    responese = ['Dad???', 'Shouldn\'t you be doing more coding questions', 'Compounding interest is the most powerful force in the world']
    return random.choice(responese)
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
