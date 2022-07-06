from pprint import pprint   
def generate_user_response(messsaging_text):

        response = None
    
        if messsaging_text=="hello" or  messsaging_text=="hey" or messsaging_text=="hi" :
                 response="Hello i'm bot"
        elif messsaging_text=="what's the price of iphone cover" or messsaging_text=="iphone"  :
                 response ="the price of all iphone covers 100LE"
        elif messsaging_text=="what's the price of samsung cover" or messsaging_text=="samsung" :
                 response ="the price of samsung covers start with 75LE"
        elif messsaging_text=="what's the price of huawei cover" or messsaging_text=="huawei" :
                 response ="the price of huawei covers start with 50LE"
        elif messsaging_text=="Hm" or messsaging_text=="hm":
                 response ="what's type of your phone"
        elif messsaging_text=="bye" or messsaging_text=="Thanks" or messsaging_text=="thanks":
                 response ="bye dear"
        else:
                 response = "sorry, i didn't understand your message!"
        return response
print("hello")
print(generate_user_response("hello"))
print("hm")
print(generate_user_response("hm"))
print("iphone")
print(generate_user_response("iphone"))

