# Writeup 9 - Forensics II

Name: Egor Reznikov
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Egor Reznikov


## Assignment details

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?
    142.93.136.81

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
    nmap was the tool that was used due to the hackers attempting to look at all the ports to find a vulnerable port.

3. What are the hackers' IP addresses, and where are they connecting from?
    159.203.113.181, Clifton, New Jersey, United States, North America

4. What port are they using to steal files on the server?
    55914, 21

5. Which file did they steal? What kind of file is it? Do you recognize the file?
    find_me.jpeg

6. Which file did the attackers leave behind on the server?
    greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.
    One countermeasure to prevent this attack would be blacklisting an ip if you see that they are doing a port scan. One example we learned in class was that if you attempt to facebook.com, Facebook will blacklist your ip so that no one on your network can access the website. In the capture file you can see a bunch of different ports being scanned and you can see the source ip.
### Part 2 (55 Pts)
1. When was greetz.fpff generated?
    2019-03-27 00:15:05

2. Who authored greetz.fpff?
    fl1nch

3. List each section, givnig us the data in it and it's type.
    Section Type: ASCII
    Section Length 24
    TEXT: Hey you, keep looking :)
    Section Type: COORD
    Section Length 16
    COORDINATES: 52.336035 4.880673
    Section Type: PNG
    Section Length 202776
    Section Type: ASCII
    Section Length 44
    TEXT: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
    Section Type: ASCII
    Section Length 80
    TEXT: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

4. Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.
    CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
    CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}