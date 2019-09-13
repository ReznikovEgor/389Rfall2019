# Writeup 2 - OSINT

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov

## Assignment Writeup

### Part 1 (45 pts)

1. Eric Norman

2. http://wattsamp.net/

3. https://www.instagram.com/ejnorman84/
    I first used https://osintframework.com/ to find a site to lookup usernames. https://namechk.com/ is the site used and it said that an Instagram was created with this username.
   http://wattsamp.net/index.html
    I found this from the instagram bio. This website is for the company Eric Norman works at and lists his position as Control Specialist.

   whois wattsamp.net
   This command shows some information such as the company location in El Paso, Texas, a phone number, and Eric Normans email ejnorman84@gmail.com.
    Eric Norman
    Organization:
    1300 Adabel Dr
    El Paso
    TX
    79835
    US
    +1.2026562837
    ejnorman84@gmail.com

4. 157.230.179.99 DigitalOcean LLC. North Bergen, New Jersey, United States, North America 07047 (40.793,-74.0247)
    I found this ip used the command ping wattsamp.net. This is gave me the ip address. I used maxmind.com to find the location of the server.
   216.239.32.109
   216.239.34.109
   216.239.36.109
   216.239.38.109
    These are ip addresses that I found from dnsdumpster.com when I searched wattsamp.net. These are addresses are for google domains.

5. wattsamp.net/robots.txt

6. 22 ssh
   80 http
   1337 waste
    I found these ports by running nmap on wattsamp.net -p 1-2000

7. Linux 2.4.37
    I ran the command nmap 157.230.179.99 -O to find out what operating system the DigitalOcean server is running on

8. CMSC389R-{html_h@x0r_lulz}
    This was in the index.html
   CMSC389R-{Do_you-N0T_See_this}
    This was text from dnsdumpster.com when I searched wattsamp.net
   CMSC389R-{n0_indexing_pls} 
    This was from wattsamp.net/robots.txt

### Part 2 (75 pts)
To do this part of the assignment, I would have find out how to beat the captcha and interate through the words in rockyou.txt. To beat the captcha, I extracted the numbers and the operator and compute the answer. I had to change the types of the data from recv into a string to work with it. After breaking the captcha, I sent the answer, the username (ejnorman84), and finally the password attempt. I had this iterate through the rockyou.txt. After a while, I found out that the password was hello1. Once I had this I used nc 157.230.179.99 1337, passed the captcha, entered the user name and password. Once I was in the system shell, I just started looking around the directory and eventually found flag.txt in the home directory. I used cat flag.txt to print the flag.

CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}
