#import stdin
from sys import stdin
# set count variable
count = 1
# for line in input file: check for language
for line in stdin:
    line = line.strip()
    casetext = 'Case ' + str(count) + ': '
    # if language match, print according to problem
    if line == '#':                 #exit
        exit()
    elif line == 'HELLO':           #eng
        print(casetext + 'ENGLISH')
    elif line == 'HOLA':            #spa
        print(casetext + 'SPANISH')
    elif line == 'HALLO':           #ger
        print(casetext + 'GERMAN')
    elif line == 'BONJOUR':         #fre
        print(casetext + 'FRENCH')
    elif line == 'CIAO':            #ita
        print(casetext + 'ITALIAN')
    elif line == 'ZDRAVSTVUJTE':    #rus
        print(casetext + 'RUSSIAN')
    else:
        print(casetext + 'UNKNOWN')
    count += 1
