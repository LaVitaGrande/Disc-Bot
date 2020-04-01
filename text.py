
""" Place to stick longer strings and other text formatting for DnD bot, 
so they dont clutter up useful code blocks.
    Command response strings are named after the command.
"""

help_text = ("DnD bot supports the following actions:\n"
    "!roll - rolls dice in XdY+Z format.  When called with no arguments rolls D20\n"
    "!advantage - rolls 2 D 20 and takes the higher\n"
    "!disadvantage - like advantage but worse\n"
    "each command has a extra help with examples e.g. \'!roll help\'"
)

# help strings in a dictionary, keys are bot command strings
help = {
    "showcontext" : "Used to show information from the current context.\n",
    "advantage" : "Rolls for advantage using DnD 5th Ed rules.\n"
    "Rolls 2 twenty sided dice and takes the higher value.\n"
    "If it is given a value it assumed that is a modifier to the roll.\n"
    "So !advantage -3 rolls 2 dice, takes the higher value, and subtracts 3 from it.",
    "disadvantage" : "Rolls for disadvantage using DnD 5th Ed rules.\n"
    "Rolls 2 twenty sided dice and takes the lower value.\n"
    "Takes all of the same inputes as !roll.\n"
    "So !disadvantage 5 rolls 2 dice, takes the lower value, and adds 5 to it.",
    "roll" : "General rolling function.  Accepts wide range of XdY+Z rolls.\n"
    "Examples:\n"
    "!roll 3d6+2 - rolls D6 3 times and adds 2.\n"
    "!roll d8-1  - rolls a single D8 and subtracts 1.\n"
    "!roll 2D4+1 is the same as 2 d 4 + 1 - Spacing and caps shouldn't matter.\n"
    "!roll 5     - rolls a d20 and adds 5.  A number by itself is treated as modified d20 roll",
    "dndhelp" : "Inception levels of help on the help function recommended by !help"
}

# some commands will have multiple response options in arrays
advantage = ["Managed to pull some of that Patrick Rothfuss bullshit eh?",
    "Angling for optimum position has paid off!",
    "Time for the rogue to roll every d6 in reach."]

disadvantage = ["What have we told you about drinking and dicing?",
    "Situational awareness isn't your strong point, is it?",
    "Hopefully this is the DM rolling.  If not..."]
    