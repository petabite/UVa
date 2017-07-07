# import stdin
from sys import stdin
def main():
    # loop for line in input:
    for line in stdin:
        #if line = 0 0 0 0:
        if line == '0 0 0 0':
            # exit
            exit()
        #else:
        else:
            line = [x.strip() for x in line]
            print(line)
            # line = [int(x) for x in line]
            # print(line)
            #create empty int var to store total degrees
            total_degrees = 0
            #do the turns/do the combo

            #strip lines and convert to int

            #print end degrees

if __name__ == '__main__':
    main()
