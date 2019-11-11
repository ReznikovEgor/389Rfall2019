import sys
import struct
import time
import binascii

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp = struct.unpack("<L", data[8:12])
author = struct.unpack("<8s", data[12:20])
section = struct.unpack("<L", data[20:24])

section = section[0]
author = author[0].decode()
timedate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp[0]))



if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timedate)
print("AUTHOR: %s" % author)
print("SECTION %d" % int(section))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
i = 1
offset = 24
while i <= section:
    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    offset+=8
    
    #1, 6, 8, 1, 1

    # SECTION_ASCII (0x1)
    if stype == 1:
        print("Section Type: ASCII")
        print("Section Length %d" % slen)
        text = struct.unpack("{}s".format(slen), data[offset:offset+slen])
        print("TEXT: " + text[0].decode())
    # SECTION_UTF8 (0x2) -- UTF-8-encoded text.
    # if stype == 2:
    # SECTION_WORDS (0x3) -- Array of words.
    # if stype == 3:
    # # SECTION_DWORDS (0x4) -- Array of dwords.
    # if stype == 4:
    # # SECTION_DOUBLES (0x5) -- Array of doubles.
    # if stype == 5:
    # # SECTION_COORD (0x6) -- (Latitude, longitude) tuple of doubles.
    if stype == 6:
        print("Section Type: COORD")
        print("Section Length %d" % slen)
        cords = struct.unpack("dd", data[offset:offset+slen])
        print("COORDINATES: " + "{}".format(cords[0]) + " " + "{}".format(cords[1]))
    # # SECTION_REFERENCE (0x7) -- The index of another section.
    # if stype == 7:
    # SECTION_PNG (0x8) -- Embedded PNG image.
    if stype == 8:
        print("Section Type: PNG")
        print("Section Length %d" % slen)
        png_head = binascii.unhexlify("89504e470d0a1a0a")
        f = open('png.png', 'wb')
        f.write(png_head)
        f.write(data[offset:offset+slen])
    # # SECTION_GIF87 (0x9) -- Embedded GIF87.
    # if stype == 9:
    # # SECTION_GIF89 (0xA) -- Embedded GIF89.
    # if stype == 10:


    offset+=slen
    i+=1