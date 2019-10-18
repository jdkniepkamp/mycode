#!usr/bin/env python3
import os
import fnmatch

def find (pattern, path):
    result = []
    for root, dirs, files, in os.walk(path,):
        for name in files:
            if fnmatch.fnmatch(name,pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("What am in looking for? example... *.txt")
lookwhere = input("What is the path in which I should search? ")
print(find(lookfor, lookwhere))
