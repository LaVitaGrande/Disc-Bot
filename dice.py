from random import randint
import re

# Dice rolling logic for DnD bot.

"""Regex that breaks a request of XdY+Z down and puts number of dice into group 1,
size of dice into group 4 and +/- modifiers into group 6.
Designed to be very tolerant of input variation.  
All of these evaluate to the same thing:
    3d6+1
    3 D6 + 1
    3D 6 +1
    3d6 1
    3 6 +1
"""
rollparse = re.compile(r"^((\d*)*)\s*(d|D)*\s*((\d*)*)\s*(\+\s*(\d*)*|-\s*(\d*)*|(\d*))$")

# dice roller func, defaults to 1d20+0
def roller(size=20, rolls=1, mod=0):
    total = 0
    for _ in range(rolls):
        total+= randint(1, size)
    return total+mod

# parses input from request using regex and tries to figure out how much data was provided
def request_reponse(request):
    parsed = rollparse.match(request)
    value = 0
    if (parsed[1] and parsed[4] and parsed[6]):  # full request
        value = roller(rolls=int(parsed[1]), size=int(parsed[4]),  mod=int(parsed[6].replace(" ","")))
    elif (parsed[1] and parsed[4]):                # just dice and size
        value = roller(rolls=int(parsed[1]), size=int(parsed[4]))
    elif ((parsed[3]=="d" or parsed[3]=="D") and parsed[4] and parsed[6]):   # single die plus mod
        value = roller(size=int(parsed[4]),  mod=int(parsed[6].replace(" ","")))
    elif ((parsed[3]=="d" or parsed[3]=="D") and parsed[4]):   # single die no mod
        value = roller(size=int(parsed[4]))
    elif (not(parsed[3]=="d" or parsed[3]=="D") and (parsed[6] or parsed[1]) ):   # if just a number assume D20 with mod
        if parsed[6]:
            value = roller(mod=int(parsed[6].replace(" ","")))  # will be this if they used + or -
        else:
            value = roller(mod=int(parsed[1]))  # plain number with no sign will be in bucket 1
    else:  # anything else roll D20
        value = roller()
    return value
