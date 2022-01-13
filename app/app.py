from flask import Flask
from flask import request, jsonify
from flask.helpers import make_response
from twil_vendor import send, register, change
from flask_swagger_ui import get_swaggerui_blueprint

import os
import toml

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# App Configs
app = Flask(__name__)
app.config["DEBUG"] = True

#Swagger Configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Soccer API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Vendors Configs
config = toml.load(os.path.join(ROOT_DIR, "config.toml"))
VENDORS = list(config["vendor"])
acvite_vendor = VENDORS[0] # Twili 1 (vendor 1) is selected by default when the system is running for the first time or after restarting the system.

print(acvite_vendor)

@app.post("/send")
def send_sms() :
    try :
        req = request.get_json()
        if req["number"] is None or req["message"] is None :
            return make_response(
                jsonify(response = {
                    "message": f"Bad request! number and message must be not null!",
                    "status": False
                }), 403
            )
        target = req["number"]
        message = req["message"]
        vendor = send(to=target, msg=message, vendor=acvite_vendor)

        return make_response(
            jsonify(response = {
                "message": f"Message successfully sent to {target} by using vendor {vendor}",
                "status": True
            }), 200
        )
    except Exception as e:
        return make_response(
            jsonify(response = {
                "message": e,
                "status": True
            }), 500
        )

# We can only use this with premium twilio account
@app.post("/register")
def register_number() :
    try :
        req = request.get_json()
        number = req["number"]
        register(number=number)
        return make_response(
            jsonify(response = {
                "message": f"Number {number} is successfully registered!",
                "status": True
            }), 201
        )
    except Exception as e:
        return make_response(
            jsonify(response = {
                "message": e.msg,
                "status": True
            }), 500
        )

@app.post("/switch")
def switch_vendor():
    try :
        req = request.get_json()
        if req["vendor_id"] is None :
            return make_response(
                jsonify(response = {
                    "message": "vendor_id must be not null!",
                    "status": False
                }), 403
            )
        
        if not any(vendor["id"] == req["vendor_id"] for vendor in VENDORS):
            return make_response(
                jsonify(response = {
                    "message": "Vendor not found!",
                    "status": False
                }), 404
            )

        selected_vendor = [vendor for vendor in VENDORS if vendor["id"] == req["vendor_id"]][0]
        global acvite_vendor
        acvite_vendor = selected_vendor
        change(acvite_vendor)

        print(f"Vendor is switched to {acvite_vendor['name']} (ID = '{acvite_vendor['id']}')")

        return make_response(
            jsonify(response = {
                "message": f"Vendor is switched to {acvite_vendor['id']}",
                "status": True
            }), 201
        )

    except Exception as e:
        return make_response(
            jsonify(response = {
                "message": e.args[0],
                "status": True
            }), 500
        )

if __name__ == "__main__" :
    app.run()