#import stdin
from sys import stdin
def main():
#read first line
    def format_line(line):
        line = line.split(' ')
        # print(line)
        line = [x.strip() for x in line]
        # print(line)
        line = [int(x) for x in line]
        return line
    def read_info_line():
        line = stdin.readline()
        if line == '':
            exit()
        line = format_line(line)
        # print(line)
        global participants
        global budget
        global hotels
        global weeks_to_choose_between
        participants = line[0]
        budget = line[1]
        hotels = line[2]
        weeks_to_choose_between = line[3]
        #store vals as vars
        #for h in range of hotels, read two lines down
    while True:
        read_info_line()
            #for each week, loop thru availible hotels
        costs_within_budget = []
        for h in range(hotels):
            total_costs = []

            price_per_person = format_line(stdin.readline())
            available_beds_for_each_weekend = format_line(stdin.readline())
            # print(available_beds_for_each_weekend)
            for available_beds in available_beds_for_each_weekend:
                if participants <= available_beds:
                    total_costs.append(participants * price_per_person[0])
            # print(total_costs)
            for cost in total_costs:
                # print(total_costs)
                if cost <= budget:
                    costs_within_budget.append(cost)
        costs_within_budget.sort()
        # print(costs_within_budget)
        if len(costs_within_budget) > 0:
            print(costs_within_budget[0])
        else:
            print('stay home')
            #compare these numbers to number of participants, if n <= beds: multiply by cost. store this value.

            #compare these numbers if within budget . print smallest. if no such, print 'stay home'
if __name__ == '__main__':
    main()
