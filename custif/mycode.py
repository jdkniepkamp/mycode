#!/usr/bin/env python3
choice ='0'
while choice =='0':
    print("Choose One....")
    print("1: What do you want to do today?")
    print("2: What is your favorite color?")
    print("3: What is your quest")
    print("4: What is the meaning of life, the universe, and everything?")
    print("5: What is the air-speed velocity of a swallow?")

    choice = input ("Please make a choice: ")

    if choice == "5":
        print("African or European?  I don't know that?!!?!!")
        break
    elif choice == "4":
        print("42")
        break
    elif choice == "3":
        print("To find the HOLY GRAIL!!")
        break
    elif choice == "2":
        print("Blue... WAIT! No- GREEN!  AAAAAAaaaaa......")
        break
    elif choice == "1":
        print("The same thing we do every day.  Plan to take over the world...")
        break
    else:
       getName = input("What is your name?....")
       print(f"{getName.title()}, you have chosen unwisely.")
        
