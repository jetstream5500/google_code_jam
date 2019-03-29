import sys
import math
import random

if __name__ == '__main__':
    #fin = open('out.txt', 'w')
    t = int(raw_input())
    for n in range(t):
        #fin.write('n+1: %d\n' % (n+1))
        a = int(raw_input())
        #fin.write('a: %d\n' % (a))
        size = max(3, int(math.sqrt(a))+1)
        grid = [[False]*(size+1) for x in range(size+1)]
        counts = [[9]*(size-2) for x in range(size-2)]
        #fin.write('%d\n' % (size))

        while True:
            max_i = -1
            max_j = -1
            max_val = -1
            for i,row in enumerate(counts):
                for j,e in enumerate(row):
                    if e > max_val:
                        max_i = i
                        max_j = j
                        max_val = e

            print('%d %d' % (max_i+3, max_j+3))
            sys.stdout.flush()

            x, y = tuple(map(int, raw_input().split()))
            #fin.write('x, y: %d %d\n' % (x, y))

            if not grid[x-1][y-1]:
                grid[x-1][y-1] = True
                for r in range(x-4, x-1):
                    for s in range(y-4, y-1):
                        if r >= 0 and s >= 0 and r<(size-2) and s<(size-2):
                            counts[r][s]-=1

            if x == -1 and y == -1:
                #fin.close()
                sys.exit(0)
            elif x == 0 and y == 0:
                break

    #fin.close()
