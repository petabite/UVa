from sys import stdin
import re
def main():
    for line in stdin:
        length = re.findall('[a-zA-Z]+', line)
        print(len(length))
if __name__ == '__main__':
    main()
