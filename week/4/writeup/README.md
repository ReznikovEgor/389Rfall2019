# Writeup 2 - Pentesting

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov

## Assignment Writeup

### Part 1 (45 pts)
CMSC389R-{p1ng_as_a_$erv1c3}

nc wattsamp.net 1337 -> 157.230.179.99 & cat /home/flag.txt

The first thing I looked at was what would happen if I ran nc wattsamp.net 1337. This prompted me to input the ip address. Since we know that wattsamp.net is vulnerable to command injection I tried inputing the ip & ls to see what would show up. This showed me a list of directories that was similar to the one in assignment 2. The first directory I checked for flag.txt was /home/ since that's where it was before. Luckily it was there again and I was able to find the flag by inputing 157.230.179.99 & cat /home/flag.txt after running nc wattsamp.net 1337. Eric could create a whitelist for allowed commands and/or character so that you can not use the &, |, or ; operator. These need to be fixed or other hackers would be able to access their directory and obtain valuable information from wattsamp.net directory.
While doing part 2, I found out that you do not have to input the whole ip address. To command inject, you can just input 1 & cmd after using ncat. This is another issue that should be fixed, you are able to access the directory without knowing the ip, so requiring the exact ip address could provide some security. The main way to stop the command injection is by having a login before accessing the home directory. You need to have usernames and more complex password requirements such as having a minimum for numbers, upper/lower letters, and special characters. Another thing that would help with security that the University of Maryland does is require a change of password every few months. Another security provision that UMD uses is two-factor authentication might also help security and not allow malicious hackers to access information since the user has a different account to verify their login. Also this would show if someone has attempted to login who is not authorized.


### Part 2 (55 pts)

For this part, the main thing I need to keep track up is the path. You need to keep track of where you are in the directory so that you can look around all the different directories. Cd is the command used for traversing and there are several ways to use cd such cd .. and cd bin/systemd. I used different cases to cover .. slashes after cd and you always have to check that a directory is valid. Another issue that I had to cover was if you were going to use multiple commands in one line, Ex. cd home & ls & cat home/flag.txt. Whenever ls was used, I used the current path and sent "1 & ls curr_path" so that it would display the content of the current directory without showing the user having to see the request for the ip address and having to nc. If the user exited the shell using "exit", the path would reset to the default path. Showing the help menu was simple, since it was only 4 print statments. For pull, I needed to use cat to see what was in the txt file using the <remote-path> and write the text into a txt file to where the <local-path> was.