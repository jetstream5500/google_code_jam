def parse_time(time):
    vals = time.split(':')
    return int(vals[0])*60+int(vals[1])

if __name__ == '__main__':
    with open('B-large-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            turnaround_time = int(fin.readline())
            num_a_trips, num_b_trips = tuple(map(int,fin.readline().split()))

            trips = []
            for i in range(num_a_trips):
                trip = fin.readline().split()
                trip = map(parse_time, trip)
                trip.append('A')
                trips.append(tuple(trip))
            for i in range(num_b_trips):
                trip = fin.readline().split()
                trip = map(parse_time, trip)
                trip.append('B')
                trips.append(tuple(trip))

            trips.sort()
            a = 0
            b = 0

            while len(trips) > 0:
                start = 0
                end = 0
                letter = ''
                indices = []
                for i, trip in enumerate(trips):
                    if i == 0:
                        indices.append(i)
                        start, end, letter = trip
                        if letter == 'A':
                            a+=1
                        else:
                            b+=1
                        end+=turnaround_time
                    else:
                        start2, end2, letter2 = trip
                        if letter != letter2 and end <= start2:
                            start = start2
                            end = end2+turnaround_time
                            letter = letter2
                            indices.append(i)

                for i in indices[::-1]:
                    trips.pop(i)


            print("Case #" + str(n+1) + ": " + str(a) + " " + str(b))
