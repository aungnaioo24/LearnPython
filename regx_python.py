# regular expression
import re  # this is the module for reg_x

txt = "The rain in spain"
x = re.search("^The.*spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")
