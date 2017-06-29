from sys import stdin

def main():
    casenum = 1
    testcases = int(stdin.readline())
    while testcases != 0:
        line = stdin.readline()
        line = line.strip()
        line = line.split()
        line = [int(x) for x in line]
        students = int(line[0])
        del line[0]
        line.sort()
        print('Case ' + str(casenum) + ': ' + str(line[-1]))
        students -= 1
        casenum += 1
        testcases -= 1

if __name__ == '__main__':
    main()
