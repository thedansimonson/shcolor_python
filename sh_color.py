"""
Contains all formatting strings for shell, \033[32m especially the colors.\033[39m 

If you just want to list through colors use:
    COLOR_LIST
    COLOR_LIST_BRIGHT
    COLOR_LIST_NORMAL

For background colors:
    BG_LIST
    BG_LIST_BRIGHT
    BG_LIST_NORMAL

To clear, use COLOR_DEFAULT and BG_DEFAULT.
To clear effects, use CLEAR_ALL

"""

#http://misc.flogisoft.com/bash/tip_colors_and_formatting

# TEXT COLOR #
COLOR_DEFAULT = "\033[39m"
COLOR_BLACK =   "\033[30m"
COLOR_RED =     "\033[31m"
COLOR_GREEN =   "\033[32m"
COLOR_YELLOW =  "\033[33m"
COLOR_BLUE =    "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN =    "\033[36m"

COLOR_LIGHTGRAY = "\033[37m"
COLOR_DARKGRAY = "\033[90m"
COLOR_LIGHTRED = "\033[91m"
COLOR_LIGHTGREEN = "\033[92m"
COLOR_LIGHTYELLOW = "\033[93m"
COLOR_LIGHTBLUE = "\033[94m"
COLOR_LIGHTMAGENTA = "\033[95m"
COLOR_LIGHTCYAN = "\033[96m"
COLOR_WHITE = "\033[97m"

COLOR_LIST_BRIGHT = [COLOR_DEFAULT, COLOR_BLACK, COLOR_RED, COLOR_GREEN,
                     COLOR_YELLOW, COLOR_BLUE, COLOR_MAGENTA, COLOR_CYAN]
COLOR_LIST_NORMAL = [COLOR_LIGHTGRAY, COLOR_DARKGRAY, COLOR_LIGHTRED, 
                     COLOR_LIGHTGREEN, COLOR_LIGHTYELLOW, COLOR_LIGHTBLUE,
                     COLOR_LIGHTMAGENTA, COLOR_LIGHTCYAN, COLOR_WHITE]
COLOR_LIST = COLOR_LIST_BRIGHT + COLOR_LIST_NORMAL

# TEXT BG #
BG_DEFAULT = "\033[49m"
BG_BLACK =   "\033[40m"
BG_RED =     "\033[41m"
BG_GREEN =   "\033[42m"
BG_YELLOW =  "\033[43m"
BG_BLUE =    "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN =    "\033[46m"

BG_LIGHTGRAY = "\033[47m"
BG_DARKGRAY = "\033[100m"
BG_LIGHTRED = "\033[101m"
BG_LIGHTGREEN = "\033[102m"
BG_LIGHTYELLOW = "\033[103m"
BG_LIGHTBLUE = "\033[104m"
BG_LIGHTMAGENTA = "\033[105m"
BG_LIGHTCYAN = "\033[106m"
BG_WHITE = "\033[107m"

BG_LIST_BRIGHT = [BG_DEFAULT, BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, 
                  BG_BLUE, BG_MAGENTA, BG_CYAN]
BG_LIST_NORMAL = [BG_LIGHTGRAY, BG_DARKGRAY, BG_LIGHTRED, BG_LIGHTGREEN, 
                  BG_LIGHTYELLOW, BG_LIGHTBLUE, BG_LIGHTMAGENTA, 
                  BG_LIGHTCYAN, BG_WHITE]
BG_LIST = BG_LIST_BRIGHT + BG_LIST_NORMAL


# EFFECTS #
SET_BOLD =        "\033[1m"
SET_DIM =         "\033[2m"
SET_UNDERLINED =  "\033[4m"
SET_BLINK =       "\033[5m"
SET_REVERSE =       "\033[7m"
SET_HIDDEN =       "\033[8m"

# RESET #
CLEAR_ALL =         "\033[0m"
CLEAR_BOLD =        "\033[21m"
CLEAR_DIM =         "\033[22m"
CLEAR_UNDERLINED =  "\033[24m"
CLEAR_BLINK =       "\033[25m"
CLEAR_REVERSE =       "\033[27m"
CLEAR_HIDDEN =       "\033[28m"

