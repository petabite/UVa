from sys import stdin

def main():
    testcases = stdin.readline()
    testcases = int(testcases)
    case_number = 0
    while testcases != 0:
        case_number += 1
        number_of_walls = stdin.readline()
        number_of_walls = int(number_of_walls)
        if number_of_walls == 1:
            stdin.readline()
            print("Case " + str(case_number) + ": 0 0")
        else:
            wall_heights = stdin.readline()
            wall_heights = wall_heights.strip()
            wall_heights = wall_heights.split(' ')
            wall_heights = [int(x) for x in wall_heights]
            high_jumps = 0
            low_jumps = 0
            for idx, wall in enumerate(wall_heights):
                if idx == len(wall_heights) - 1:
                    break
                else:
                    if wall_heights[idx + 1] > wall_heights[idx]:
                        high_jumps += 1
                    if wall_heights[idx + 1] < wall_heights[idx]:
                        low_jumps += 1
            print("Case " + str(case_number) + ": " + str(high_jumps) + ' ' + str(low_jumps))
        testcases -= 1
if __name__ == '__main__':
    main()
