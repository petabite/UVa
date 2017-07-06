#import stdin
from sys import stdin

def main():
    #loop thru each line in the input file
    #and print them.
    for line in stdin:
        print(line, end ='')
if __name__ == '__main__':
    main()
