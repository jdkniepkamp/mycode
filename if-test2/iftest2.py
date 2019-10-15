#!/usr/bin/env python3
ipchk = input("Enter and IP Address here: ")


if ipchk == "192.168.70.1":
    print ("Looks like the IP address of the Gateway was set: " + ipchk)
elif ipchk:
    print("Looks like some data was entered...")
else:
    print("You didn't provide any input...")

