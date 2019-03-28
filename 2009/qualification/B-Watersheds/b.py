def pretty_print_table(table):
    for row in table:
        print(' '.join(row))

if __name__ == '__main__':
    with open('B-large-practice.in.txt') as fin:
        num_test_cases = int(fin.readline())

        for n in range(num_test_cases):
            rows, cols = tuple(map(int, fin.readline().split()))

            table = []
            answer_table = [['']*cols for i in range(rows)]

            for i in range(rows):
                row = map(int, fin.readline().split())
                table.append(row)

            #print(table)

            letter = 97

            for i in range(rows):
                for j in range(cols):
                    #print('--------')
                    prev_depth = table[i][j]+1
                    depth = table[i][j]
                    location = (i, j)
                    while depth < prev_depth:
                        options = [depth]
                        locations = [location]
                        if location[0] > 0:
                            options.append(table[location[0]-1][location[1]])
                            locations.append((location[0]-1, location[1]))
                        if location[1] > 0:
                            options.append(table[location[0]][location[1]-1])
                            locations.append((location[0], location[1]-1))
                        if location[1] < cols-1:
                            options.append(table[location[0]][location[1]+1])
                            locations.append((location[0], location[1]+1))
                        if location[0] < rows-1:
                            options.append(table[location[0]+1][location[1]])
                            locations.append((location[0]+1, location[1]))

                        #print(options)
                        prev_depth = depth
                        depth = min(options)
                        location = locations[options.index(min(options))]


                    #print(location)
                    if answer_table[location[0]][location[1]] == '':
                        answer_table[i][j] = chr(letter)
                        answer_table[location[0]][location[1]] = chr(letter)
                        letter+=1
                    else:
                        answer_table[i][j] = answer_table[location[0]][location[1]]

            print('Case #%d:' % (n+1))
            pretty_print_table(answer_table)
