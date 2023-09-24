#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4 
else :
	print("Invalid amount of Arguments")
	print("Syntax : python3 scanner.py <ip>")
	
	
# Printing Banner

print("-"*50)
print("Scanning Target " + target)
print("Time Started : " + str(datetime.now()))
print("-"*50)

try :
	start_range = int(input("Enter starting range of Port : "))
	end_range = int(input("Enter end range of Port : "))
	for port in range( start_range , end_range+1 ) :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #Returns an error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is Open".format(port))
		s.close()
except KeyboardInterrupt :
	print("\nExiting Program")
	sys.exit()
except socket.gaierror :
	print("Hostname could not be resolved ")
	sys.exit()
except socket.error :
	print("Couldn't connect to server.")
	sys.exit() 
