if __name__ == '__main__':
    with open('A-large-practice.in.txt', 'r') as fin:
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            num_snappers, k = tuple(map(int, fin.readline().split()))
            snaps_to_loop = 2**num_snappers
            if k % snaps_to_loop == snaps_to_loop-1:
                print('Case #%d: ON' % (n+1))
            else:
                print('Case #%d: OFF' % (n+1))
