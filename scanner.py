import sys 
import socket 
from datetime import datetime 
    
if len(sys.argv) == 2: 
    
    target = sys.argv[1]
else: 
    print("Invalid ammount of Argument")
    print("Usage:python3 scanner.py <IP Address>")
    sys.exit()

print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 
ports=[]
try: 
    
    for port in range(1,65535): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
        
        #print(int((port/65535)*100),"%")

        sys.stdout.write("Scanning ... %s %%\r" % (int((port/65535)*100)))
        sys.stdout.flush()

        result = s.connect_ex((target,port)) 
        if result ==0: 
            ports.append(port)
        s.close()  
        
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit() 

for i in ports:
    print("Port ",i," in open")

nmap="nmap -A -p"
for i in ports:
    if i==ports[-1]:
        nmap=nmap+str(i)+" "
    else:
        nmap=nmap+str(i)+","

nmap=nmap+str(target)
print(nmap)