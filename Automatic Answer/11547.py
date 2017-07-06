#import stdin
from sys import stdin
#read the testcase line
testcases = int(stdin.readline().strip())
#loop thru this
for case in range(testcases):
    num = stdin.readline()
    # print(num)
    num = int(num.strip())
    #do the operation for each
    num = num * 567
    num = num / 9 + 7492
    num = num * 235 / 47
    num = num - 498
    num = int(num)
    num = str(num)
    print(num[-2])
#take the number in the tens column
#print it
