# import stdin
from sys import stdin
def main():
    # loop for line in input:
    for line in stdin:
        line = line.strip()
        #if line = 0 0 0 0:
        if line == "0 0 0 0":
            # exit
            exit()
        #else:
        else:
            #strip lines and convert to int
            line = line.split(' ')
            line = [int(x) for x in line]
            #create empty int var to store total degrees
            total_degrees = 0
            start = line[0]
            first = line[1]
            second = line[2]
            third = line[3]
            total_degrees += 720                            #turn clockwise twice
            total_degrees += (start - first + 40) % 40 *9
            total_degrees += 360 + (second - first +40) % 40 *9
            total_degrees += (second - third + 40) %40 * 9
            print(total_degrees)
if __name__ == '__main__':
    main()
