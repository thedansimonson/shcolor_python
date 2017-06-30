# shcolor_python
A library with strings for changing colors in bash.

For example, if you want to print out the string "There will be blood." with
the word "blood" in red, you can do:

    import sh_color
    print "There will be "+sh_color.COLOR_RED+"blood"+sh_color.COLOR_DEFAULT+"."

Features:
* `COLOR_.*` for text color
* `BG_.*` for background color
* `SET_.*` for effects (underline, bold, etc.)
* `COLOR_DEFAULT`, `BG_DEFAULT`, and `CLEAR_ALL` for resetting text color, background, and effects.
