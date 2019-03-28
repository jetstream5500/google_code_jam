def gcd_condenser(a):
    while len(a) > 1:
        for i in range(len(a)-1):
            a[i] = gcd(a[i], a[i+1])
        a.pop()

    return a.pop()

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

if __name__ == '__main__':
    with open('B-large-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            vals = map(int, fin.readline().split())
            vals.pop(0)
            vals = list(set(vals))
            vals.sort()
            diffs = []

            for i in range(len(vals)-1):
                diffs.append(vals[i+1]-vals[i])

            big_t = gcd_condenser(diffs)

            if vals[0] % big_t == 0:
                print('Case #%d: %d' % (n+1, 0))
            else:
                print('Case #%d: %d' % (n+1, big_t-(vals[0]%big_t)))
