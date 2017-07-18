from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = testcases.strip()
    testcases = int(testcases)
    while testcases != 0:
        stores = stdin.readline()
        locations = stdin.readline()
        locations = locations.strip()
        locations = locations.split(' ')
        locations = [int(x) for x in locations]
        farthest = max(locations)
        closest = min(locations)
        print((farthest - closest)*2)
        testcases -= 1
if __name__ == '__main__':
    main()
