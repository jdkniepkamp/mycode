#!/user/bin/python3
loginfail = 0
loginsuccess = 0
with open("/home/student/mycode/attemptedlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            print("The IP of the unauthorized user is:", line.split(" ")[-1], end="")
        elif "- - - - -] Loaded 2 encryption keys" in line:
            loginsuccess += 1

print("The number of failed login attempts is", loginfail)
print("The number of successful logins is", loginsuccess)
