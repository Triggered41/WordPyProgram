import os

os.system("clear")
run = ["open", "show", "run", "tell", "where", "plz", "do", "what", "screen"]

def can_run():
    for i in range(len(run)):
        if run[i] in user_input:
            return True

while True:
    
    print("===============World of automation===============\n")

    print("Please tell what you want me to do: ", end = '')
    
    user_input = input()
    user_input = user_input.lower()
    
    if (can_run()):
        print("\n")
        if ("clear" in user_input):
            os.system("clear")
        elif ("list" in user_input) or ("directory" in user_input):
            if ("all" in user_input) or ("everything" in user_input) or ("hidden" in user_input):
                os.system("ls -a")
            else:
                os.system("ls")
        elif ("print" in user_input):
            text = input("text to print: ")
            print("\n")
            os.system("echo " + str(text))
        elif ("make" in user_input) or ("create" in user_input):
            dir_name = input("name the directory: ")
            os.system("mkdir " + dir_name)
        elif ("processes" in user_input):
            os.system("ps -a")
        elif ("calendar" in user_input):
            os.system("cal")
        elif ("date" in user_input):
            os.system("date")
        elif ("time" in user_input):
            os.system("time")
        elif ("sleep" in user_input):
            t = str(input("for how many seconds: "))
            os.system("sleep " + t)
        elif ("ipaddress" in user_input):
            os.system("ifconfig")
        elif ("copy" in user_input):
            file_name = input("file to copy: ")
            destination = input("path: ")
            os.system("cp " + file_name + " " + destination)
        elif ("path" in user_input) and ("current" in user_input):
            os.system("pwd")
        elif ("locate" in user_input):
            os.system("locate")
        elif ("find" in user_input):
            os.system("find")
        elif ("help" in user_input):
            cmd = input("for which command: ")
            os.system(cmd + " --help")
        elif ("create" in user_input) and ("file" in user_input):
            file = input("name the file")
            os.system("cat > " + file)
        elif ("user" in user_input):
            os.system("whoami")
        elif ("BG" in user_input):
            os.system("$")
        elif ("manual" in user_input):
            os.system("man ")
        elif ("bash" in user_input):
            file = input("path pf file: ")
            os.system("bash " + file)
        elif ("FG" in user_input):
            os.system("fg")
        elif ("nano" in user_input):
            name = input("name of file: ")
            os.system("nano " + name)
        elif ("touch" in user_input):
            name = input("name files: ")
            os.system("touch " + name)
        elif ("vi" in user_input):
            name = input("file name: ")
            os.system("vi")
        elif ("vim" in user_input):
            name = input("file name: ")
            os.system("vim")
        elif ("path" in user_input):
            os.system("echo $PATH")
        elif ("exit" in user_input):
            exit()
        else:
            print("Nothing Found!")
        print("\n")
    else:
        print("\nI did not understand!\n")
            