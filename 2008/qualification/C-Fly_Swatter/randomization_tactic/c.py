import random
import math
#import matplotlib.pyplot as plt

def dist(x, y):
    return math.sqrt(x**2 + y**2)

def inside_ring(R, x, y):
    return (dist(x,y) <= R)

def intersects_ring(f, R, t, x, y):
    return (dist(x,y)+f >= R-t)

def intersects_strings(f, r, g, x, y):
    vertical_string = round(x/(g+2*r)) * (g+2*r)
    if abs(x-vertical_string) <= r+f:
        #print('hit vert', abs(x-vertical_string))
        return True

    horizontal_string = round(y/(g+2*r)) * (g+2*r)
    if abs(y-horizontal_string) <= r+f:
        #print('hit hori', abs(y-horizontal_string))
        return True

    return False

if __name__ == '__main__':
    with open('test.in', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            vals = fin.readline().split()
            f = float(vals[0])
            R = float(vals[1])
            t = float(vals[2])
            r = float(vals[3])
            g = float(vals[4])

            # RANDOM Fly Generation
            hits = 0.0
            misses = 0.0
            count = 0
            size = 1000000
            inside_x = []
            inside_y = []
            while count < size:
                x = random.random()*(R+t)
                y = random.random()*(R+t)
                if inside_ring(R, x, y):
                    if intersects_ring(f, R, t, x, y) or intersects_strings(f, r, g, x, y):
                        hits+=1
                    else:
                        misses+=1
                        #print("f: " + str(f), "R: " + str(R), "t: " + str(t), "r: " + str(r), "g: " + str(g), x, y)
                        inside_x.append(x)
                        inside_y.append(y)
                    count+=1

            print(hits/(hits+misses))
            #plt.scatter(inside_x, inside_y)
            #plt.show()
