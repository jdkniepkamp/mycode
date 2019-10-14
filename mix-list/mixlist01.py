#! user/bin/env python3
my_list = ["192.169.0.5", 5060, "UP"]
print ("The first item on the list (IP): " + my_list[0] )
print ("The second item on my list (Port): " + str(my_list[1]) )
print ("The last item on my list (Stat): " + my_list[2] )



new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]


print(f"When I {new_list[5]} into IP addreess {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}." ) 
