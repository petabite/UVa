from sys import stdin

def main():
    testcases = int(stdin.readline())
    while testcases != 0:
        num_of_instructions = int(stdin.readline())
        position = 0
        instructions = []
        while num_of_instructions != 0:
            instruction = stdin.readline()
            instruction = instruction.strip()
            instructions.append(instruction)
            def robot_action(instruction):
                nonlocal position
                if instruction == 'LEFT':
                    position -= 1
                elif instruction == 'RIGHT':
                    position += 1
                else:
                    instruction = instruction.split(' ')
                    same_as = instruction[2]
                    robot_action(instructions[int(same_as)-1])
            robot_action(instruction)
            num_of_instructions -= 1
        print(position)
        testcases -= 1
if __name__ == '__main__':
    main()
