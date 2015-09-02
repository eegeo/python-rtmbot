import time
import random

crontable = []
outputs = []

buddies = ["tim.jenks", "mark.simpson", "scott", "malcolm.brown", "ian.hutchinson", "jonty", "oliver.norton", "vimarsh.raina", "paul.harris", "john.bell"]
cursor = -1

def usage():
    return "usage: :cow: buddy"

def commandname():
    return "buddy"

def process_message(data, plugin):
    global cursor
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
                try:
                    while True:
                        cursor = cursor + 1
                        if cursor > len(buddies)-1:
                            cursor = 0
                        the_buddy = buddies[cursor]
                        user_id = data['user'] #requester's UID
                        slack_client = plugin.getbot().get_slack_client()
                        user = slack_client.server.users.find(user_id)
                        if not user == None:
                            if not the_buddy == user.name:
                                break
                        else:
                            break

                    outputs.append([data['channel'], "*cow kicks*: @{0}".format(the_buddy)])
                except:
                    raise
                    outputs.append([data['channel'], usage()])
