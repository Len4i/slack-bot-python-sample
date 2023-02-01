import sys, os
import logging

from flask import Flask
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from controllers.greeting import Greeting
from controllers.ondemand_env import OndemandEnv

###########################
###### Logs handling ######
###########################
logging.basicConfig()

####################
###### Config ######
####################
load_dotenv()
app = App(token=os.getenv("SLACK_BOT_TOKEN"))
flask_app = Flask(__name__)


##############################################
#### Flask HTTP "is_alive" Event Listener ####
##############################################
@flask_app.route("/healthz", methods=["GET"])
def is_alive():
    return "ok"


##############################
#### Register controllers ####
##############################
Greeting(app)
OndemandEnv(app)



###################################
#### Start slack and flask apps ####
###################################
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.connect()
    flask_app.run(debug=False, port=8888, host='0.0.0.0')
