import math

def print_points(ps):
    for p in ps:
        print('{} {} {}'.format(*p))

def rotate_x(ps, angle):
    for i,p in enumerate(ps):
        ps[i] = (   ps[i][0],
                    math.cos(angle)*ps[i][1] - math.sin(angle)*ps[i][2],
                    math.sin(angle)*ps[i][1] + math.cos(angle)*ps[i][2],)

def rotate_z(ps, angle):
    for i,p in enumerate(ps):
        ps[i] = (   math.cos(angle)*ps[i][0] - math.sin(angle)*ps[i][1],
                    math.sin(angle)*ps[i][0] + math.cos(angle)*ps[i][1],
                    ps[i][2])

def orth_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[2]-p2[2])**2)

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)

def area(p1, p2, p3):
    a = orth_dist(p1, p2)
    b = orth_dist(p2, p3)
    c = orth_dist(p1, p3)
    s = (a+b+c)/2

    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def region_area(ps):
    return area(ps[2], ps[4], ps[6]) + area(ps[6], ps[0], ps[2]) + area(ps[4], ps[5], ps[3]) + area(ps[3], ps[2], ps[4]) + area(ps[0], ps[1], ps[3]) + area(ps[3], ps[2], ps[0])

if __name__ == '__main__':
    num_test_cases = int(raw_input())
    for n in range(num_test_cases):
        a = float(raw_input())
        ps = [  (-0.5, -0.5, -0.5),
                (-0.5, 0.5, -0.5),
                (0.5, -0.5, -0.5),
                (0.5, 0.5, -0.5),
                (0.5, -0.5, 0.5),
                (0.5, 0.5, 0.5),
                (-0.5, -0.5, 0.5),
                (-0.5, 0.5, 0.5)    ]

        if a <= 1.414213:
            prev = 1
            direction = 1
            angle_movement = 0.01
            for i in range(1000):
                rotate_z(ps, direction*angle_movement)
                new_area = region_area(ps)
                if abs(new_area-a) > abs(prev-a):
                    direction*=-1
                    angle_movement/=10
                prev = new_area
        else:
            rotate_z(ps, math.pi/4)
            prev = region_area(ps)
            direction = 1
            angle_movement = 0.01
            for i in range(1000):
                rotate_x(ps, direction*angle_movement)
                new_area = region_area(ps)
                if abs(new_area-a) > abs(prev-a):
                    direction*=-1
                    angle_movement/=10
                prev = new_area

        centers = [midpoint(ps[4], ps[3]), midpoint(ps[2], ps[6]), midpoint(ps[0], ps[3])]
        print('Case #%d:' % (n+1))
        print_points(centers)
