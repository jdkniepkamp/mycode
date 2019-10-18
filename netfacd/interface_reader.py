#!/usr/bin/env python3
"""MyCode"""
import netifaces
print(netifaces.interfaces() )
for i in netifaces.interfaces():
    print('\n***************Details of Interface - ' + i + '****************')
    try:
        print('MAC: ', end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) 
        print('IP: ', end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        raise ValueError('This error occured for whatever reason')
    except:
        print('Could not collect adapter information....')
