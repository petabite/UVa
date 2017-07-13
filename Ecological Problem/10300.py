from sys import stdin

def main():
    testcases = int(stdin.readline())
    while testcases != 0:
        farmers = int(stdin.readline())
        total_premium = 0
        while farmers != 0:
            params = stdin.readline()
            params = params.strip()
            params = params.split(' ')
            params = [int(x) for x in params]
            farmyard_size = params[0]
            animals = params[1]
            if animals == 0:
                total_premium += 0
            else:
                environment_friendliness = params[2]
                average_space_per_animal = farmyard_size/animals
                farmer_premium_per_animal = average_space_per_animal*environment_friendliness
                final_premium = farmer_premium_per_animal*animals
                total_premium += final_premium
            farmers -= 1
        print(round(total_premium))
        testcases -= 1

if __name__ == '__main__':
    main()
