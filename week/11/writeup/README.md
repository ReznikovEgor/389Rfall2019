# Writeup 1 - Web I

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

The first thing I did was look around the website and look at the url. The Fortnite 0-day url was http://142.93.136.81:5000/item?id=0. I first tried to get a webshell to work but a quick look at piazza made me realize that we just needed an SQL injection. The SQL injection I was going to attempt was "admin' OR '1'='1'-- -" This lead me to a page that said "ERROR: ATTEMPTED SQL INJECTION DETECTED". This means that the website has something detecting certain characters and not letting the user use an SQL injection but I changed 'OR' to '||' and I was given the flag.

CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

1. I inputed <script>alert()</script>

2. A hint lead me to use onerror and img source, so I inputed <img src='' onerror=window.alert()> in a forum post

3. For this one, I saw that the url would change when you click on different tabs so I used what I had in the last level in the url of this level. https://xss-game.appspot.com/level3/frame#<img src='' onerror=window.alert()>

4. I inputed ');alert(' to preform the xss. The "');" part tells the website to end the onload function and then the rest sends the alert.

5. I changed the end of the url from 'next=confirm' to 'next=javascript:alert()', press go, and then press the next button to preform the xss.

6. I used the url from the hint https://www.google.com/jsapi?callback=foo and changed 'foo' to 'alert' to run alert(). I pasted this to replace the file path in the url. The level won't allow the use of 'https' so I changed the file too 'HTTPS://www.google.com/jsapi?callback=alert' and this preformed the xss.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
