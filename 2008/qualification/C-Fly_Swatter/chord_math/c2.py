# Works but is very slow!!!

import math

def midpoint(a, b):
    ''' Computes the midpoint between the 2 given points (a, b) '''
    return ((a[0]+b[0])/2, (a[1]+b[1])/2)

def dist(a, b=(0,0)):
    ''' Computes the distance between the 2 given points (a, b) '''
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def area(p1, p2, p3):
    ''' Computes the area of the triangle which is formed by the given 3 points
    (p1, p2, p3).  Utilizes heron's formula'''

    a = dist(p1, p2)
    b = dist(p2, p3)
    c = dist(p1, p3)
    s = (a+b+c)/2

    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def compute_chord_area(a, b, r):
    ''' "Sectional Area" represents a "slice" of the circle (like a pizza
    slice!) while "Trianglular Area" represents the triangle formed when
    discluding the chord from the "Sectional Area".'''

    #print('computing chord area ...')
    theta_left = math.atan(a[1]/a[0])
    theta_right = math.atan(b[1]/b[0])
    percent = abs(theta_left-theta_right) / (2*math.pi)
    #print('percent', percent)
    sectional_area = percent * math.pi * (r)**2
    #print("sectional", sectional_area)
    trianglular_area = area(a, b, (0,0))
    #print("triangle", trianglular_area)
    #print('ending ...')

    return sectional_area - trianglular_area

if __name__ == '__main__':
    with open('C-large-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            #print(n)
            vals = fin.readline().split()
            f = float(vals[0])
            R = float(vals[1])
            t = float(vals[2])
            r = float(vals[3])
            g = float(vals[4])
            inner_radius = R-t-f

            #print(f, R, t, r, g)

            raq_strings = int(round(R/(g+2*r)) + 1)

            #print(raq_strings)

            gap_area = 0

            for i in range(raq_strings):
                for j in range(raq_strings):
                    #print('----------------')
                    ps = [  (i*(g+2*r) + (r+f), j*(g+2*r) + (r+f)),
                            (i*(g+2*r) + (r+f), j*(g+2*r) + (r+g-f)),
                            (i*(g+2*r) + (r+g-f), j*(g+2*r) + (r+f)),
                            (i*(g+2*r) + (r+g-f), j*(g+2*r) + (r+g-f))  ]

                    if (ps[0][0] > ps[2][0] or ps[0][1] > ps[1][1]):
                        continue
                    else:
                        inside = []
                        outside = []
                        for p in ps:
                            if dist(p) < inner_radius:
                                inside.append(p)
                            else:
                                outside.append(p)

                        if len(inside) == 1:
                            p = inside[0]
                            left = (p[0], math.sqrt((inner_radius)**2 - p[0]**2))
                            right = (math.sqrt((inner_radius)**2 - p[1]**2), p[1])
                            chord_area = compute_chord_area(left, right, inner_radius)
                            remaining_area = (left[1]-p[1])*(right[0]-p[0])*0.5
                            gap_area += chord_area + remaining_area
                        elif len(inside) == 2:
                            p1 = inside[0]
                            p2 = inside[1]
                            left = 0
                            right = 0
                            if (p1[0] == p2[0]):
                                left = (math.sqrt((inner_radius)**2 - p1[1]**2), p1[1])
                                right = (math.sqrt((inner_radius)**2 - p2[1]**2), p2[1])
                            else:
                                left = (p1[0], math.sqrt((inner_radius)**2 - p1[0]**2))
                                right = (p2[0], math.sqrt((inner_radius)**2 - p2[0]**2))

                            chord_area = compute_chord_area(left, right, inner_radius)
                            remaining_area = dist(p1, p2) * ((dist(p1, left) + dist(p2, right))/2)
                            gap_area += chord_area + remaining_area
                        elif len(inside) == 3:
                            left = (math.sqrt((inner_radius)**2 - inside[1][1]**2), inside[1][1])
                            right = (inside[2][0], math.sqrt((inner_radius)**2 - inside[2][0]**2))
                            chord_area = compute_chord_area(left, right, inner_radius)
                            remaining_area = area(inside[0], inside[1], left) + area(inside[0], left, right) + area(inside[0], right, inside[2])
                            gap_area += chord_area + remaining_area
                        elif len(inside) == 4:

                            gap_area += dist(inside[0], inside[1])*dist(inside[0], inside[2])

            print("Case #%d: %f" % (n+1, round(1 - (4*gap_area / (math.pi * R**2)), 6)))
