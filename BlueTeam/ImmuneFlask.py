# Same Flask App modified to handle DOS
# Reference code https://stackoverflow.com/questions/24222220/block-an-ip-address-from-accessing-my-flask-app-on-heroku
# Reference code (modified) https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_dos_and_ddos_attack.htm
import flask

from scapy.all import *
# import struct  # unused

# import request  # unused
nest_dict = {}
# from datetime import datetime  # unused

threshold = 20  # max number of requests before being blocked
app = flask.Flask(__name__)


def update_firewall(ip_address, add):
    if add:
        print("Firewall settings updated to ban: ", ip_address)
    else:
        print("Firewall settings updated to re-allow: ", ip_address)


@app.before_request
def block_method():

    ip_address = flask.request.remote_addr
    t1 = time.time()

    print("Request from: ", ip_address)
    print("Access Route: ", flask.request.access_route)
    print("Current Dict: ", nest_dict)
    print("Time of Request: ", t1)
    for el in nest_dict:
        if nest_dict[el]['time'] - t1 > 100:
            update_firewall(el, False)
            del nest_dict[el]
            print("Updated Dict: ", dict)
    if ip_address in nest_dict:
        nest_dict[ip_address]['requests'] = nest_dict[ip_address]['requests'] + 1
        print("Current Dict: ", nest_dict[ip_address]['requests'])

        print(nest_dict[ip_address]['requests'])
        print("Time since last request: ", t1 - nest_dict[ip_address]['time'])
        if t1 - nest_dict[ip_address]['time'] < 100:
            if nest_dict[ip_address]['requests'] > threshold:  # and (nest_dict[ip_address] < threshold + 10):
                line = "DDOS attack is Detected from " + ip_address + " with " + str(
                    nest_dict[ip_address]['requests']) + " requests. \nBlocking access !"
                print(line)
                '''file_txt.writelines(line)
                file_txt.writelines(ip_address)
                file_txt.writelines("\n")'''
                update_firewall(ip_address, True)
                flask.abort(403)
        else:
            nest_dict[ip_address]['requests'] = 1
        nest_dict[ip_address]['time'] = t1
    else:
        nest_dict[ip_address] = {}
        nest_dict[ip_address]['requests'] = 1
        nest_dict[ip_address]['time'] = t1
        print("Updated Dict: ", dict)


@app.route('/')
def hello():
    return "Hello {}!".format(flask.request.remote_addr)


if __name__ == '__main__':
    app.run()
