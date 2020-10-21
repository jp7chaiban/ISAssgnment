# Same Flask App modified to handle DOS
# Reference code https://stackoverflow.com/questions/24222220/block-an-ip-address-from-accessing-my-flask-app-on-heroku
# Reference code (modified) https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_dos_and_ddos_attack.htm
import flask

import struct
import request
dict = {}
from datetime import datetime


threshold = 20  # max number of requests before being blocked
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

            line = "DDOS attack is Detected from " + ip_address + " with " + \
                   str(dict[ip_address]) + " requests. \nBlocking further access !"
            print(line)

            flask.abort(403)
    else:
        dict[ip_address] = 1
        print("Updated Dict: ", dict)


@app.route('/')
def hello():

    return "Hello World!"


if __name__ == '__main__':
    app.run()
