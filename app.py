import random
from pymessenger.bot import Bot
from flask import Flask, request

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFpjOT0M4sBAK8SSF7LW1iV9wkZBhy6IJEyYcWpadSC6LQumypvdZAXdy0LsSaTqpxNr4t3tpxnmRuYZBr87nJ0MQdoB840IFQyT0BlE6oii1pkTY6OQdKBirErTviEqnv0Vk6xmnuJNcWrTZBlZBqNbv4vwNYHz3OFnk6hzLM40LSbZBOAZAn3bSWnIOuNzEZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

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
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == '__main__':
    app.run(debug = True)
