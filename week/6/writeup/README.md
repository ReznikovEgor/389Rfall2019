# Writeup 6 - Binaries I

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

When I first started, I just ran the called the program ./crackme. This returned "Did you even try disassembling?" and this showed me somewhat how main was working. If you fail in main, the program would divert from which ever check you are at and print a string. If you type anything after the file call, it tells you that multiword arguments must be in "". This occurs with you fail check1. I looked at check1 and found that there was a strcmp will the string "Oh God" above a couple lines. I typed ./crackme "Oh God" into my terminal and was told me "I wish you cared more about the environment". This got me on the train of though of using an environment variable. In check2 there was a getenv call right after a lea and push with "FOOBAR". This tells us that the program is expecting an environment variable named "FOOBAR". I little farther down there is a string that says "seye my ". I attempted setting "FOOBAR" to this value but it did not work so I set "FOOBAR" to " my eyes" with (export FOOBAR=" my eyes") and I passed that second check. Check3 starts with a prompt "open sesame" and has a open, read, and close call so I have to create a file. I used touch sesame and this prompted me with "like this but more", so I thought I have to put something in sesame. While I attempted to put "123" and still got the same prompt so I put 10 characters in and got "hard-coded string comparison". I ran (strings ./readme) to see if there was any strings that seemed valuable. I couldn't find anything but check3 has 9 cases and a cmp call in each of them. I learned about how to change a hex into a string in Binary Ninja by pressing 'r' and I found that the comparisons each had a character that spelled " theyburn" and I put " they burn" into sesame and ran (./crackme "Oh God") to receive the flag.