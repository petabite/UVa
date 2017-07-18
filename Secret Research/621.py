from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = testcases.strip()
    testcases = int(testcases)
    while testcases != 0:
        line = stdin.readline()
        line = line.strip()
        if line == '1' or line == '4' or line == '78':
            print("+")
        elif line.endswith('35'):
            print('-')
        elif line.startswith('9') and line.endswith('4'):
            print('*')
        else:
            print('?')
        testcases -= 1
if __name__ == '__main__':
    main()
