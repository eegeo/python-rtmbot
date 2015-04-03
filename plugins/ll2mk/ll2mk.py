import time
from maths.lat_long import LatLong
from spaces.cube_map import lat_long_to_morton_key
from spaces.morton_key_helpers import create_morton_key_debug_string

crontable = []
outputs = []

def usage():
    return "usage: :cow: ll2mk lat_degrees long_degrees level"

def commandname():
    return "ll2mk"

def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
        	   try:
                    lat_degrees = float(splits[2])
                    long_degrees = float(splits[3])
                    level = int(splits[4])
                    lat_long = LatLong.from_degrees(lat_degrees, long_degrees)
                    key = lat_long_to_morton_key(lat_long, level)
                    response = create_morton_key_debug_string(key)
                    outputs.append([data['channel'], response])
        	   except:
                    outputs.append([data['channel'], usage()])