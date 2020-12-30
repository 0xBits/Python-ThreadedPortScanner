import time
import socket as Socky
import threading
from queue import Queue

Print_Thread_Lock = threading.Lock()
Socky.setdefaulttimeout(0.20)

InputHost = input('Enter the IP to be port scanned: ')
InputHost2IP = Socky.gethostbyname(InputHost)
InputBeginPort = int(input('Enter STARTING port (0 to 65535): '))
InputEndPort = int(input('Enter ENDING port (0 to 65535): '))
print('Port scan initiated on: [' + InputHost2IP + "] on ports between (" + str(InputBeginPort) + ") and (" + str(InputEndPort) + ")")

def scanport(portno):
    s = Socky.socket(Socky.AF_INET, Socky.SOCK_STREAM)
    try:
        connection = s.connect((InputHost2IP, portno))
        with Print_Thread_Lock:
            print(portno, 'is open (TCP)')
        connection.close()
    except:
        pass

def threader():
    while True:
        worker = inqueue.get()
        scanport(worker)
        inqueue.task_done()

inqueue = Queue()
startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(int(InputBeginPort), int(InputEndPort)):
    inqueue.put(worker)

inqueue.join()
print('Execution time:', (time.time() - startTime), "seconds.")