import requests, random, datetime, sys, time, os

from colorama import Fore, Back, Style
from termcolor import colored
from banners import ban

def russia():
    os.system("python3 bombRU.py")

def ukraine():
    print(ban.ukraine)
    input()
    main()

def batya():
    print(ban.batya)
    input()
    main()

def exit():
    os.system("clear")
    print('Прощай! Надеюсь я тебе больше не нужен...')
    sys.exit()

def main():
    os.system('clear')
    print(ban.banner)
    print(ban.menu)
    num_menu = input("<0~ ")
    if num_menu == "":
       main()
    if num_menu == "1":
        russia()
    if num_menu == "2":
        ukraine()
    if num_menu == "3":
        batya()
    if num_menu == "4":
        exit()
main()
