#!/usr/bin/env python3
""" CODE STUFF"""
import numpy as np
import matplotlib.pyplot as plt

N=4
localnetMeans = (20,35,30,35)
wanMeans = (25, 32, 34, 20)
ind = np.arange(N)
width = 0.35

# Where to display p1
p1 = plt.bar(ind, localnetMeans, width)
#Stack p2
p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

#Describe the table
plt.ylabel("Length of Outage (mins)")
plt.title("2018 network summary")
plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

#Display
plt.savefig("/home/student/mycode/graphing/2018summary.png")
