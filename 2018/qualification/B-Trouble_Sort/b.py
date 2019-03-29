def trouble_sort(a):
    done = False
    while not done:
        done = True
        for i in range(0, len(a)-2):
            if a[i] > a[i+2]:
                done = False
                temp = a[i]
                a[i] = a[i+2]
                a[i+2] = temp

def trouble_sort2(a):
    odds = a[::2]
    evens = a[1::2]
    odds.sort()
    evens.sort()

    for i,e in enumerate(evens):
        odds.insert(2*i+1, e)

    return odds

if __name__ == '__main__':
    num_test_cases = int(raw_input())
    for n in range(num_test_cases):
        size = int(raw_input())
        a = map(int, raw_input().split())
        #print(a)
        a = trouble_sort2(a)
        #print(a)
        printed = False
        prev = float('-inf')
        #print(prev)
        for i, num in enumerate(a):
            if num >= prev:
                prev = num
            else:
                print('Case #%d: %d' % (n+1, i-1))
                printed = True
                break

        if not printed:
            print('Case #%d: OK' % (n+1))
