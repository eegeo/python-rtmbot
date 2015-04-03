import time
import random

crontable = []
outputs = []

def usage():
    return "usage: :cow: whoami"

def commandname():
    return "whoami"

def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
                try:
                    user_id = data['user']
                    slack_client = plugin.getbot().get_slack_client()
                    user = slack_client.server.users.find(user_id)
                    if user == None:
                        outputs.append([data['channel'], "unknown"])
                    else:
                        outputs.append([data['channel'], "@{0}".format(user.name)])      
                except:
                    outputs.append([data['channel'], usage()])