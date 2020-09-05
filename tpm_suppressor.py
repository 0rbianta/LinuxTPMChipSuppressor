import os
import time

def restoreSystemFile():
    os.system("clear")
    bckup = open("blacklist", "r")
    if(bckup.mode == "r"):
        dump = bckup.read()
        SYS_File = open("/etc/modprobe.d/blacklist", "w")
        SYS_File.write(dump)
        SYS_File.close()
        print("Restore complete!")
        input("Press any key to continue...")
        os.system("clear")
        print("See you...")
    else:
        print("Error.\nblacklist not found!\nDo you have backup file? This file is created by the program, but maybe something has happened to it.")

def selectMainOperation():
    os.system("clear")
    print("Select your operation.\n1)Run fix code!\n2)Restore modded files.")
    usr=int(input("USER>> "))
    if(usr==1):
        checkSystemFileExist()
    elif(usr==2):
        restoreSystemFile()
    else:
        os.system("clear");
        print("Error while taking your number.")
        print("Possible reasons:\nLeaving a space at the beginning or end of the number.\nEntering a character other than the numbers in the option.")

def checkSystemFileExist():
    try:
        bckup = open("blacklist", "w")
        os.system("clear")
        print("Dumping file...")
        time.sleep(1.5)
        dump=os.popen("cat /etc/modprobe.d/blacklist").read()
        print(dump)
        time.sleep(1.0)
        os.system("clear")
        print("Dumping Successful.")
        print("Continues...")
        time.sleep(2.0)
        os.system("clear")

        if("blacklist tpm" in dump):
            print("Your system files already modded. You can restore them.")
            exit()

        bckup.write(dump)
        bckup.close()

        os.system("echo blacklist tpm_infineon >> /etc/modprobe.d/blacklist")
        os.system("echo blacklist tpm >> /etc/modprobe.d/blacklist")
        os.system("echo blacklist tpm_bios >> /etc/modprobe.d/blacklist")

        os.system("clear")
        print("Your system has been successfully refreshed. TPM Chip will disable when you reboot your computer.")
        print("\n IF YOU WILL HAVE A ERROR then you can restore your modded system files back by backup file.")
        print("\n Follow me...\n")
        print("Twitter:0rbianta\nGitHub:0rbianta\nAnd nothing else to say.")
        input("Press any key to continue...")
        print("Reboot your system to disable TPM Chip.")
        print("1)Reboot now\n2)Reboot later manual")
        usr = int(input("USER>> "))
        if (usr == 1):
            os.system("reboot")
            exit()
        elif(usr==2):
            os.system("clear")
            print("Good bye!")

    except:
        print("Error\n/etc/modprobe.d/blacklist not found!\nProgram can't continue.")

def main():

    user_profile=os.popen("whoami").read()
    if("root" in user_profile):
        os.system("clear")
    else:
        print("Please run as root.")
        exit()

    i1=os.popen("toilet TPM").read()
    i2=os.popen("toilet Chip").read()
    i3=os.popen("toilet Suppressor").read()
    print(i1+"\n"+i2+"\n"+i3)


    time.sleep(1.0);
    os.system("clear");
    print("This software will not fix your TPM problem. It just silences it. To summarize TPM simply: It is a security chip in your computer. Some computers provide an option to turn this chip off in the BIOS settings. Check your BIOS settings for this option before using this utility. If such an option is not available in BIOS like me, you may run into problems. No problem. This software will disable the TPM chip across the computer. This is not a solution but a very good way to avoid the problem. Finally, I would like to remind you that all responsibilities belong to you.\n")
    print("Do you accept that all responsibility belongs to you?")
    print("1)Accept\n2)Refuse\n")
    usr=int(input("USER>> "))
    if(usr==1):
        selectMainOperation()
    elif(usr==2):
        os.system("clear")
        print("Exiting...")
    else:
        os.system("clear");
        print("Error while taking your number.")
        print("Possible reasons:\nLeaving a space at the beginning or end of the number.\nEntering a character other than the numbers in the option.")

if __name__ == '__main__':
    main()
