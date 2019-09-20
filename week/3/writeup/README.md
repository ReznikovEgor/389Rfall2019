# Writeup 3 - OPSEC SE

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov

## Assignment Writeup

### Part 1 (40 pts)
One way to attempt to get some information from Eric Norman is striking up a conversation with him and asking some questions like where are you from. Most people don’t think anything is out of the blue if you ask them where they are from, which covers the place you are born question. Another thing you could bring up is a useful Chrome extension like Momentum and see what he says to find out what browser he uses. Where I’m from, there has been a bunch of new banks opening and has become a talking point for some people, so you could mention something about a new bank opening and asking Eric if he uses that bank. This could lead to him saying what bank he uses. If we know what bank he uses, we can use his phone number from the 2nd homework and pose as his bank. You could start the conversation saying that there has been a recent breach and that he needs to change some security questions that the bank recommends. In a position of authority over him, posing as his bank you could ask his pin number as confirmation and ask his mother’s maiden name and the name of his first pet to cover the recommended security questions.


### Part 2 (60 pts)
The first thing I would tell Eric Norman to try to fix, would be the weak passwords. Wattsamp could have a requirement that includes a capital letter, lower case letter, a number, a password length minimum, and a special character like most websites have. Another feature you could add would be having an account be locked if a password was entered wrong several times in a row. This would stop programs like the one we wrote that iterates through a large list of common password. Another issue that needs to be fixed would be the open port 1337 which allows anyone to attempt to login. This needs to be closed or a firewall needs to be put in place to stop people from seeing the open ports. Finally he would have to have a way to not allow personal information to get out. I found his personal information from the command whois, so if you could place a block on whois this would not allow me to use his phone number to other information from him.
