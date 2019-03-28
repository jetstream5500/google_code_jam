import functools

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def solve(L):
  y = L[0]
  L1 = [abs(x - y) for x in L]
  g = functools.reduce(gcd, L1)
  if y % g == 0:
    return 0
  else:
    return g - (y % g)

if __name__ == '__main__':
    with open('B-small-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            vals = map(int, fin.readline().split())
            vals.pop(0)
            print('Case #%d: %d' % (n+1, solve(vals)))
