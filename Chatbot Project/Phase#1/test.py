import os , sys
from flask import Flask , request
import json
app = Flask(__name__)

VERIFICATION_TOKEN = "hello"

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook() :
    printmsg("I am here")
    data = request.get_json()
    printmsg(data)
    printmsg(request.data)

    return "okk",200

def printmsg(msg) :
    print(msg)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True ,port =80)
