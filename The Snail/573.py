from sys import stdin

def main():
    #if h = 0: end
    lines = [x.strip() for x in stdin.readlines()]
    for line in lines:
        line = line.split(' ')
        line = [int(x) for x in line]
        # print(line)
        if line[0] == 0:
            exit()
        else:
            wellheight = line[0]
            # print(wellheight)
            distanceclimbed = line[1]
            # print(distanceclimbed)
            slide = line[2]
            # print(slide)
            fatigue = line[3]/100 * distanceclimbed
            # print(fatigue)
            day = 1
            dis = distanceclimbed
            if 0 <= dis <= wellheight:
                dis = dis - slide
                print('dis after day 1: ' + str(dis))
                while 0 <= dis <= wellheight:
                    print('dis climbed : ' + str(distanceclimbed))
                    day += 1
                    print('day ' + str(day) + " starting: " + str(dis))
                    print('new distance - fatigue: ' + str(distanceclimbed - fatigue))
                    if distanceclimbed >= 0:
                        dis = dis + distanceclimbed - fatigue
                        distanceclimbed = distanceclimbed - fatigue
                    print('dis: ' + str(dis))
                    if 0 <= dis <= wellheight:
                        dis = dis - slide
                    print('day: ' + str(day) + ' end dis: ' + str(dis))
            if dis < 0:
                print('failure on day ' + str(day))
            if dis > wellheight:
                print('success on day ' + str(day))
            else:
                print('something wrong')
    #store values as vars
    #for loop for days
    # distance * fatigue - slide
    # if result is zero or less, fail
    # if 6 or above, success
    #count +=6
if __name__ == '__main__':
    main()
