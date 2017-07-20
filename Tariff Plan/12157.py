from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = testcases.strip()
    testcases = int(testcases)
    case = 0
    while testcases != 0:
        case += 1
        stdin.readline()
        call_durations = stdin.readline()
        call_durations = call_durations.strip()
        call_durations = call_durations.split(' ')
        call_durations = [int(x) for x in call_durations]
        total_mile = 0
        total_juice = 0
        for call in call_durations:
            mile = call//30*10
            if call % 29 >= 0:
                mile += 10
            total_mile += mile
            juice = call//60*15
            if call % 59 >= 0:
                juice += 15
            total_juice += juice
        if total_juice > total_mile:
            print('Case ' + str(case) + ': ' + 'Mile ' + str(total_mile))
        elif total_juice < total_mile:
            print('Case ' + str(case) + ': ' + 'Juice ' + str(total_juice))
        else:
            print('Case ' + str(case) + ': ' + 'Mile Juice ' + str(total_mile))
        testcases -= 1
if __name__ == '__main__':
    main()
