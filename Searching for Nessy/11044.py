from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = testcases.strip()
    testcases = int(testcases)
    while testcases != 0:
        line = stdin.readline()
        line = line.strip()
        line = line.split(' ')
        line = [int(x) for x in line]
        rows = line[0]
        columns = line[1]
        print(str((rows//3) * (columns//3)))
        testcases -= 1
if __name__ == '__main__':
    main()
