import time
from spaces.morton_key import MortonKey
from spaces.morton_key_helpers import create_morton_key_debug_string

crontable = []
outputs = []

def usage():
    return "usage: :cow: mk2ll morton_key"

def commandname():
    return "mk2ll"

def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
        	   try:
                    input_key = splits[2]
                    key = MortonKey.from_string(input_key.replace("\\", ""))
                    response = create_morton_key_debug_string(key)
                    outputs.append([data['channel'], response])
        	   except:
                    outputs.append([data['channel'], usage()])