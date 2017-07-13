from sys import stdin

def main():
    inputlines = int(stdin.readline())
    balance = 0
    while inputlines != 0:
        line = stdin.readline()
        if line.startswith('donate'):
            num = []
            for char in line:
                if char.isdigit():
                    num.append(char)

            num = int(''.join(num))
            balance += num
        else:
            print(balance)
        inputlines -= 1

if __name__ == '__main__':
    main()
