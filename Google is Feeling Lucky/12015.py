from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = int(testcases)
    case = 0
    while testcases != 0:
        case += 1
        raw_lines = []
        relevant = []
        for i in range(10):
            line = stdin.readline().strip()
            line = line.split(' ')
            raw_lines.append(line)
        urls = dict(raw_lines)
        ratings = urls.values()
        ratings = [int(x) for x in ratings]
        ratings = sorted(ratings, reverse=True)
        for key, value in urls.items():
            value = int(value)
            if value == ratings[0]:
                relevant.append(key)
        print("Case #" + str(case) + ':')
        for x in relevant:
            print(x)
        testcases -= 1
if __name__ == '__main__':
    main()
