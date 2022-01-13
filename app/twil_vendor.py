from twilio.rest import Client
import toml
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config = toml.load(os.path.join(ROOT_DIR, "config.toml"))

twilio = config["vendor"][0] # we use Twilio 1 (vendor 1) as default

def change(new_twil) :
    global twilio
    twilio = new_twil
    print(twilio)

def send(to, msg, vendor):
    try :
        client = Client(twilio["twilio_sid"], twilio["twilio_auth_token"])
        message = client.messages.create(body=msg,
                                        from_=twilio["twilio_number"],
                                        to=to,
                                        )
        return vendor["name"]
    except Exception as e:
        raise e

def register(number):
    try :
        client = Client(twilio["twilio_sid"], twilio["twilio_auth_token"])
        validation_request = client.validation_requests \
                            .create(
                                    friendly_name=number,
                                    phone_number=number
                                )
        
        print(validation_request)
    except Exception as e:
        raise e
