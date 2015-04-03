import time
import boto
import boto.ec2
import datetime
import dateutil.parser

crontable = []
outputs = []

def usage():
    return "usage: :cow: spotprice instancetype awsregion"

def commandname():
    return "spotprice"

def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
               try:
                    instance_type = splits[2]
                    availability_zone = splits[3]
                    conn = boto.ec2.connection.EC2Connection()
                    now = datetime.datetime.now()
                    two_hours_ago = now - datetime.timedelta(hours=2)

                    price_history = conn.get_spot_price_history(start_time=two_hours_ago.isoformat(), end_time=now.isoformat(), instance_type=instance_type, availability_zone=availability_zone)

                    outputs.append([data['channel'], "moo, {0} prices in {1}".format(instance_type, availability_zone)])
                    pricedata = ""
                    for p in price_history:
                       date = dateutil.parser.parse(p.timestamp)
                       pricedata = pricedata + "{0}: ${1}\n".format(date.strftime("%d/%b %H:%M"), p.price)

                    outputs.append([data['channel'], pricedata])
               except:
                    outputs.append([data['channel'], usage()])