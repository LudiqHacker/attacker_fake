from termcolor import colored
from os import system
from random import randint
from time import sleep

system("clear")

input("Press Enter to start the attack: ")
while True:
    try:
        id = randint(1, 9999999)
        chance = randint(1, 5)
        print(colored(f"[-]Attack sent to id {id}", "red"))
        if chance == 3:
            print(colored(f"[+]Data collected from id {id}", "green"))
            sleep(0.1)
        else:
            sleep(0.1)
    except:
        KeyboardInterrupt()
        system("clear")
        print("You stopped the attack!")
        choice = input("Would you like to continue the attack(y/n): ").capitalize()
        if choice == "Y":
            continue
        else:
            print("The attack was stopped successfully!")
            exit()