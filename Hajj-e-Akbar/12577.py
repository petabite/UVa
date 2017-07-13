from sys import stdin

def main():
    case = 0
    for line in stdin:
        line = line.strip()
        case += 1
        if line == '*':
            exit()
        elif line == 'Hajj':
            print('Case ' + str(case) + ': Hajj-e-Akbar')
        else:
            print('Case ' + str(case) + ': Hajj-e-Asghar')
if __name__ == '__main__':
    main()
