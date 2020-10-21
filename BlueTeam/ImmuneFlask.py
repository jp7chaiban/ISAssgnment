# Same Flask App modified to handle DOS
import flask

import struct
import request
dict = {}
from datetime import datetime

# file_txt = open("attack_DDoS.txt", 'a')
threshold = 20
app = flask.Flask(__name__)

@app.before_request
def block_method():
    t1 = str(datetime.now())
    # ip_address = request.environ.get('REMOTE_ADDR')
    ip_address = flask.request.remote_addr
    print("Request from: ", ip_address)
    print("Current Dict: ", dict)
    if ip_address in dict:
        dict[ip_address] = dict[ip_address] + 1
        print(dict[ip_address])
        if dict[ip_address] > threshold:  # and (dict[ip_address] < threshold + 10):

            line = "DDOS attack is Detected from " + ip_address + " with " + str(dict[ip_address]) + " requests. \nBlocking access !"
            print(line)
            '''file_txt.writelines(line)
            file_txt.writelines(ip_address)
            file_txt.writelines("\n")'''
            flask.abort(403)
    else:
        dict[ip_address] = 1
        print("Updated Dict: ", dict)


@app.route('/')
def hello():

    return "Hello World!"


if __name__ == '__main__':
    app.run()
