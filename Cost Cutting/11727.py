from sys import stdin, stdout

def main():
    casenum = 1
    testcases = int(stdin.readline())
    while testcases != 0:
        case = stdin.readline()
        case = case.split()
        case.sort()
        print('Case', str(casenum) + ':', case[1])
        casenum += 1
        testcases = testcases - 1

if __name__ == '__main__':
    main()
