from sys import stdin

def main():
    case = 0
    while True:
        case += 1
        supposed_to_give_treat = 0
        actually_given_treat = 0
        queries = stdin.readline()
        queries = queries.strip()
        queries = int(queries)
        if queries == 0:
            exit()
        else:
            line = stdin.readline()
            line = line.strip()
            line = line.split(' ')
            line = [int(x) for x in line]
            for num in line:
                if num > 0:
                    supposed_to_give_treat += 1
                else:
                    actually_given_treat += 1
        print("Case " + str(case) + ": " + str(supposed_to_give_treat - actually_given_treat))
if __name__ == '__main__':
    main()
