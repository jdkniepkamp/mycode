#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
if hostname == "mtg":
    print ("The hostname matches the expected configuration.")
if hostname.lower() == "mtg":
	print ("The hostname was found to be mtg")
print ("exiting script....")
