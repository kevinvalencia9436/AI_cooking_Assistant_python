__author__ = 'hemalatha_ganireddy'
from flask import Flask
app = Flask(__name__)
import os.path
import sys
import json



try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
# CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
client_access_token = '8bd3b6024a8e461f8e4e63c181882295'




#@app.route("/")
def basic():
    ai = apiai.ApiAI(client_access_token)
    request = ai.text_request()
    # request.lang = 'en'  # optional, default value equal 'en'
    # request.session_id = "unique"
    request.query = "Chicken"
    response = request.getresponse()
    #print json.loads(response.read())
    #output = json.loads(response.read())['result']["fulfillment"]["messages"][0]['speech']
    #print json.loads(response.read())['result']['fulfillment']
    output = json.loads(response.read())['result']
    output_speech = output["fulfillment"]["speech"]
    intent_name = output["metadata"]["intentName"]
    if (output_speech.rsplit(None,1)[-1] == 'chicken:'):
        ai = apiai.ApiAI("2014eca4faff41eaa164b46c965aaa52")
        request = ai.text_request()
        request.query = "yes"
        response = request.getresponse()
        output = json.loads(response.read())['result']
        output_speech = output["fulfillment"]["speech"]
        print output_speech
        intent_name = output["metadata"]["intentName"]
    print output_speech,intent_name
    return response.read()

if __name__ == '__main__':
    basic()
    #app.run()
