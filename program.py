from fileinput import filename
import os
from posixpath import dirname

while True:
    print("=========================World of automation=========================")

    print("Please tell what you want me to do")

    inp = input()
    inp = inp.lower()
    if ("open" in inp) or ("show" in inp) or ("run" in inp) or ("tell" in inp) or ("where" in inp):
        if ("clear" in inp):
            os.system("clear")
        elif ("list" in inp):
            os.system("ls")
        elif ("print" in inp):
            print("Plz Enter what you wnat me to print")
            text = input()
            os.system("echo " + text)
        elif ("make" in inp) or ("create" in inp):
            print("What do you wnat to name the directory")
            dir_name = input()
            os.system("mkdir " + dir_name)
        elif ("processes" in inp):
            os.system("top")
        elif ("calendar" in inp):
            os.system("cal")
        elif ("date" in inp):
            os.system("date")
        elif ("time" in inp):
            os.system("time")
        elif ("sleep" in inp):
            print("for how long you want me to sleep")
            t = int(input())
            os.system("sleep" + t)
        elif ("ipaddress" in inp):
            os.system("ipconfig")
        elif ("copy" in inp):
            print("Which file? do you want to copy")
            file_name = input()
            print("Where?")
            destination = input()
            os.system("cp " + file_name + " " + destination)
        elif ("check" in inp):
            os.system("pwd")
        elif ("locate" in inp):
            os.system("locate")
        elif ("find" in inp):
            os.system("find")
        elif ("help" in inp):
            os.system("--help")
        elif ("create" in inp):
            os.system("cat > ")
        elif ("user" in inp):
            os.system("whoami")
        elif ("BG" in inp):
            os.system("$")
        elif ("manual" in inp):
            os.system("man ")
        elif ("bash" in inp):
            os.system("bash ")
        elif ("FG" in inp):
            os.system("fg")
        elif ("touch" in inp):
            os.system("touch")
        elif ("vi" in inp):
            os.system("vi")
        elif ("vim" in inp):
            os.system("vim")
        elif ("exit" in inp):
            exit()
    else:
            print("Nothin Found!")
    
