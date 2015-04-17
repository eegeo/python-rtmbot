import time
import boto
import boto.ec2.cloudwatch
import datetime
import dateutil.parser

crontable = []
outputs = []

def usage():
    return "usage: :cow: awsbill"

def commandname():
    return "awsbill"

def process_message(data, plugin):
    if "text" in data:
        splits = data['text'].split(" ")
        if splits[0] == ":cow:":
            if splits[1] == commandname():
               try:
                    end = datetime.datetime.utcnow()
                    start = end - datetime.timedelta(hours=4)
                    period = 300
                    conn = boto.ec2.cloudwatch.connect_to_region('us-east-1')

                    outputs.append([data['channel'], 'approximate mapreduce account breakdown:'])
                    total = 0.0
                    for m in conn.list_metrics(metric_name=u'EstimatedCharges',namespace=u'AWS/Billing'):
                        if 'ServiceName' in m.dimensions:
                            metric_return = m.query(start, end, 'Sum')
                            if len(metric_return) > 0:
                                cost = metric_return[0]['Sum']
                                outputs.append([data['channel'], "{0} - ${1}".format(m.dimensions['ServiceName'][0], cost)])
                                total += cost

                    outputs.append([data['channel'], 'Total: *${0}*'.format(total)])


               except:
                    outputs.append([data['channel'], usage()])