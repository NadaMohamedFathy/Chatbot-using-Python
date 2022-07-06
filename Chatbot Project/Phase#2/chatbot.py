import os , sys
from flask import Flask , request
import json
from pymessenger import Bot
from utils import generate_user_response

PAGE_ACCESS_TOKEN = "EAAMd3I08aBIBAJfGilDfTs9ZB3lH0k5ZAo1sdPGDpvrFmPbSCCMQZBzz07gHVsWRtKwaTWKlj0oJNHPqL4QqDyqac920zKxQZACmlTDmZANrFwpEel19P0jbNm5NCjjv1v1VayneDJcFAjpbypG7Jx2PZBlYwS6rwhPVLU5RnGanJTZCqFUtvZAtE0CuZB4WetZBwZD"
bot = Bot(PAGE_ACCESS_TOKEN)
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
    data = request.get_json()
    printmsg(data)
    process_data(data)
    return "okk",200

def process_data(data):
    #Check if value correponding to object key is "page"
      if data["object"]=="page":
            #loop on the list correponding to entry key
             for entry in data["entry"]:
              #loop on the list correponding to the messaging key
              for messaging_event in entry["messaging"]:
                #access the messege event:
                #(1) get sender and recipient IDs
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"]
                #(2) check messege type is simple messege type
                if messaging_event.get("message"):
                   if "text" in messaging_event["message"]:#there is text key
                      messaging_text = messaging_event["message"]["text"]
                   else:
                      messaging_text = "no text"
                   printmsg( messaging_text)
                   #Ech
                   response = generate_user_response(messaging_text) 
                   bot.send_text_message(sender_id,response)
def printmsg(msg) :
    print(msg)
    sys.stdout.flush()

if __name__=="__main__":
   app.run(debug=True ,port =80)
