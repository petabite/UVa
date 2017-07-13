from sys import stdin

def main():
    testcases = int(stdin.readline())
    while testcases != 0:
        word = stdin.readline()
        if word == '':
            exit()
        else:
            if len(word) == 6:
                print(str(3))
            else:
                wordlist = []
                for i in word:
                    wordlist.append(i)
                check = list(zip(wordlist[:-1], ["o", "n", "e"]))
                lettercorrect = []
                for t in check:
                    if t[0] == t[1]:
                        lettercorrect.append(t[1])
                if len(lettercorrect) >= 2:
                    print(str(1))
                else:
                    print(str(2))
        testcases -= 1
if __name__ == '__main__':
    main()
