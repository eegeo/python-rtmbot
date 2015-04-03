import time

crontable = []
outputs = []

#todo: datadrive
documents = {
    "backlog" : "https://docs.google.com/a/kimbleoperations.com/spreadsheets/d/1NRc8hFepFDfr0O7n0hsIfXWd5kd23dCz9WydxLV7usM",
    "roadmap" : "https://docs.google.com/a/kimbleoperations.com/spreadsheets/d/1_kSOXNdhRrznYeWjcPRBQFmZsuOBJNL5QJYZ6vDYVK4",
    "cubemap" : "https://docs.google.com/a/kimbleoperations.com/spreadsheets/d/1bS8gkm3aZsDAKMueCkBmx7_LbLwzVn_F9HQdm68d-vk",
    "gisbuilds" : "https://docs.google.com/a/kimbleoperations.com/spreadsheet/ccc?key=0Ak27DpOmcG30dHRYYzg3aUs2YnJjakdYb1Z1d0xVTFE",
    "japanbuild" : "https://docs.google.com/a/kimbleoperations.com/spreadsheet/ccc?key=0Ak27DpOmcG30dHRna1FLZVNnN3ZVTHVVaU5KOWR3VFE",
    "ukbuild" : "https://docs.google.com/a/kimbleoperations.com/spreadsheets/d/1ZcSDuwD_-ziogNOT-5utVWeetc56SRFsZGxJ7L6d7kI",
    "salesfunnel" : "https://docs.google.com/a/kimbleoperations.com/spreadsheets/d/1xralOM0S5XHo9Wg3Wb3GfhScw8AHg3reBmibIf4gun8"
}

def usage():
    return "usage: :cow: docs [doc]"

def commandname():
    return "docs"

# todo: process_command (sender_uname, data, plugins, args)
def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname() and len(splits) == 2:
        	   try:
                    docs = " ".join(documents.keys())
                    outputs.append([data['channel'], "*cow knows documents*: {0}". format(docs)])
        	   except:
                    outputs.append([data['channel'], usage()])
            elif splits[1] == commandname():
                try:
                    outputs.append([data['channel'], "*moo*: " + documents[splits[2]]])
                except:
                    outputs.append([data['channel'], usage()])
