from sys import stdin

def main():
    for line in stdin:
        line = line.strip()
        if line == '-1 -1':
            exit()
        line = line.split(' ')
        line = [int(x) for x in line]
        current = line[0]
        target = line[1]
        results = []
        results.append((current-target+100)%100)
        results.append((target-current+100)%100)
        results = sorted(results)
        print(results[0])
if __name__ == '__main__':
    main()
