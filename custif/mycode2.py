#!/usr/bin/env python3
def main():
    import os
    os.system('clear')
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
            print()
            print("African or European?  I don't know that?!!?!!  AAAAAAaaaa......")
            print()
            break
        elif choice == "4":
            print()
            print("42")
            print()
            break
        elif choice == "3":
            print()
            print("To find the HOLY GRAIL!!")
            print()
            break
        elif choice == "2":
            print()
            print("Blue... WAIT! No- GREEN!  AAAAAAaaaaa......!!!")
            print()
            break
        elif choice == "1":
            print()
            print("The same thing we do every day.....plan to take over the world...!")
            print()
            break
    else:
        print()
        getName = input("What is your name?....")
        print()
        print(f"{getName.title()}, you have chosen unwisely.")
        print()
        exit()
main()
