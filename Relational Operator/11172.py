from sys import stdin, stdout

# def main():
#     line = stdin.readlines()
#     for l in line:
#         new = l.split(' ')
#         new[-1] = new[-1].strip()
#         new = list(map(int, new))
#         if len(new) > 1:
#             if new[0] > new[1]:
#                 print('>')
#             elif new[0] < new[1]:
#                 print('<')
#             else:
#                 print('=')\
def main():
    num = stdin.readline()
    for val in range(int(num)):
        line = stdin.readline().split()
        if int(line[0]) < int(line[1]):
            print('<')
        elif int(line[0]) > int(line[1]):
            print('>')
        else:
            print('=')

if __name__ == '__main__':
    main()
