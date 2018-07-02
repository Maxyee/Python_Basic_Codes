import re

line = "cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*) .*',line , re.M|re.I)

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj or searchObj:
    print ("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ",matchObj.group(2))

    print ("searchObj.group() : ", searchObj.group())
    print ("searchObj.group(1) : ", searchObj.group(1))
    print ("searchObj.group(2) : ", searchObj.group(2))
else:
    print("No match!!")