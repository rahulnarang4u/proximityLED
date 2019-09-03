
import requests
import conf
from boltiot import Bolt
import json, time


mybolt = Bolt(conf.bolt_api_key, conf.device_id) #Create object to fetch data

response = mybolt.serialRead('10')
print (response)

def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False


while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduino
    data = json.loads(response)
    status_value = data['value'].rstrip()
    
    if str(status_value) == 'HIGH':
        print ("Status is", status_value)
        
        message = "Object detected in proximity!"
        telegram_status = send_telegram_message(message)
    else:
         print ("Status is LOW!",status_value)
        
    time.sleep(10)
