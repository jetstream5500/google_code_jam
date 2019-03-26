import sys

if __name__ == '__main__':
    with open('A-large-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            num_search_engines = int(fin.readline())
            search_engines = [fin.readline().rstrip('\n') for i in range(num_search_engines)]
            #print(search_engines)
            num_queries = int(fin.readline())
            queries = [fin.readline().rstrip('\n') for i in range(num_queries)]

            if num_queries == 0:
                print("Case #" + str(n+1) + ": " + str(0))
            else:
                memo_table = [[sys.maxsize]*num_search_engines for i in range(num_queries)]
                min_table = [sys.maxsize]*num_queries

                for i, q in enumerate(queries):
                    index = search_engines.index(q)
                    for j, s in enumerate(search_engines):
                        if j != index:
                            if i == 0:
                                memo_table[i][j] = 0
                            elif memo_table[i-1][j] == sys.maxsize:
                                memo_table[i][j] = min_table[i-1]+1
                            else:
                                memo_table[i][j] = memo_table[i-1][j]
                    min_table[i] = min(memo_table[i])

                print("Case #" + str(n+1) + ": " + str(min_table[-1]))
