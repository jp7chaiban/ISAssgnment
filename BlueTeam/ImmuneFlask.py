# Same Flask App modified to handle DOS
import flask
from scapy.all import Ether, ARP, srp, sniff, conf
import struct
# import request
nest_dict = {}
from datetime import datetime

# file_txt = open("attack_DDoS.txt", 'a')
threshold = 20
app = flask.Flask(__name__)

@app.before_request
def block_method():
    # ip_address = request.environ.get('REMOTE_ADDR')
    ip_address = flask.request.remote_addr
    t1 = str(datetime.microsecond)
    print("Request from: ", ip_address)
    print("Current Dict: ", nest_dict)
    print("Time of Request: ", t1)
    if ip_address in nest_dict:
        nest_dict[ip_address]['requests'] = nest_dict[ip_address]['requests'] + 1
        print("Current Dict: ", nest_dict[ip_address]['requests'])
        nest_dict[ip_address]['time'] = t1
        print(nest_dict[ip_address]['requests'])
     if nest_dict[ip_address]['time'] > 100:
        if nest_dict[ip_address]['requests'] > threshold:  # and (nest_dict[ip_address] < threshold + 10):
            line = "DDOS attack is Detected from " + ip_address + " with " + str(nest_dict[ip_address]['requests']) + " requests. \nBlocking access !"
            print(line)
            '''file_txt.writelines(line)
            file_txt.writelines(ip_address)
            file_txt.writelines("\n")'''
            flask.abort(403)
    else:
        line = "DDOS attack is Detected from " + ip_address
        print(line)
        '''file_txt.writelines(line)
        file_txt.writelines(ip_address)
        file_txt.writelines("\n")'''
        flask.abort(403)
    else:
    nest_dict[ip_address]['requests'] = 1
    print("Updated Dict: ", dict)


@app.route('/')
def hello():

    return "Hello World!"


if __name__ == '__main__':
    app.run()
