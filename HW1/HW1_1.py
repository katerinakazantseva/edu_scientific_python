import re

print('Please chose:\n1-Remove duplicates \n2-Replace Mus-M.\n3-Remove brackets ')
opt = raw_input()

if opt == "1":
    print('Enter string')
    s = raw_input()
    print(re.sub(r"(.)\1", r"\1", s))


if opt == "2":
    print('Enter string')
    s = raw_input()
    print(re.sub(r"(?<=.{1})\w+ ",". ", s))


if opt == "3":
    print('Enter string')
    s = raw_input()
    s=re.sub(r"(?<=[A-Z]{1})\w+ ",". ",s)
    s=re.sub(r"\(","",s)
    print(re.sub(r"\)","",s))
