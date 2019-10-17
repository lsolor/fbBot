import requests

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v2.6/me/'

class Bot(object):

    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    def send_text_message(self, psid, message, messaging_type="RESPONSE"):
