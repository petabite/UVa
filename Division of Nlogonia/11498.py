from sys import stdin, stdout

def main():
    query = int(stdin.readline())
    while query != 0:
        point = stdin.readline()
        x, y = point.split()
        x = int(x)
        y = int(y)
        for i in range(query):
            line = stdin.readline()
            qx, qy = line.split()
            qx = int(qx)
            qy = int(qy)
            if  qx < x and y < qy:
                print('NO')
            elif x < qx and y < qy:
                print('NE')
            elif qx < x and qy < y:
                print('SO')
            elif x < qx and qy < y:
                print('SE')
            else:
                print('divisa')
            # else:
            #     print('wut')
            #     print(x, y)
            #     print(qx, qy)

            query = query - 1
        query = int(stdin.readline())

if __name__ == '__main__':
    main()
