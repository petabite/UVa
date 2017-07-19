from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = int(testcases)
    print("Lumberjacks:")
    while testcases != 0:
        orig_lumberjacks = stdin.readline()
        orig_lumberjacks = orig_lumberjacks.strip()
        proc_lumberjacks = orig_lumberjacks.strip()
        proc_lumberjacks = proc_lumberjacks.split(' ')
        low_high_lumberjacks = sorted(proc_lumberjacks, key=int)
        low_high_lumberjacks = " ".join(low_high_lumberjacks)
        high_low_lumberjacks = sorted(proc_lumberjacks, key=int, reverse=True)
        high_low_lumberjacks = " ".join(high_low_lumberjacks)
        def all_same(items):
            return all(x == items[0] for x in items)
        if all_same(proc_lumberjacks):
            print('Unordered')
        elif orig_lumberjacks == low_high_lumberjacks or orig_lumberjacks == high_low_lumberjacks:
            print('Ordered')
        else:
            print('Unordered')
        testcases -= 1
if __name__ == '__main__':
    main()
