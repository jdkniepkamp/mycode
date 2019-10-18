#!/usr/bin/env python3

import pyexcel
def get_ip_data():
    input_ip = input("\nWhat is the IP Address? ")
    input_driver = input("What is the driver associated?" )
    d = {"IP": input_ip, "driver": input_driver}
    return d

#RUNTIME
mylistdict = []

print("Hello!  This program will make you an *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value?  Enter to continue, or enter (q) to (q)uit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input ("\nWhat is the name of the *.xls file? ")
pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')
print("The file " + filename + ".xls should be in your local directory")

