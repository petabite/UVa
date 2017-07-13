from sys import stdin

def main():
    testcases = int(stdin.readline())
    case = 0
    while testcases != 0:
        case += 1
        line = stdin.readline()
        line = line.split(' ')
        line = [x.strip() for x in line]
        line = [int(x) for x in line]
        if line[0] <= 20 and line[1] <= 20 and line[2] <= 20:
            print('Case ' + str(case) + ': good')
        else:
            print('Case ' + str(case) + ': bad')
        testcases -= 1

if __name__ == '__main__':
    main()
