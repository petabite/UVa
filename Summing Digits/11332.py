from sys import stdin

def main():
    for line in stdin:
        line = line.strip()
        if line == '0':
            exit()
        else:
            while int(line) >= 10:
                line = str(line)
                line = [str(x) for x in line]
                line = sum(int(i) for i in line)
            print(line)
if __name__ == '__main__':
    main()
