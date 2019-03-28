# Extremely slow

def compute_memo(k, groups):
    memo = []
    total = 0
    base_index = 0
    index = 0
    while base_index < len(groups):
        if total + groups[index] > k:
            memo.append((total, (index-base_index)%len(groups)))
            total -= groups[base_index]
            base_index += 1
        elif total == sum(groups):
            memo.append((total, len(groups)))
            total -= groups[base_index]
            base_index += 1
        else:
            total += groups[index]
            index = (index + 1) % len(groups)

    return memo

if __name__ == '__main__':
    with open('C-large-practice.in.txt', 'r') as fin:
        test_cases = int(fin.readline())
        for n in range(test_cases):
            R, k, N = tuple(map(int, fin.readline().split()))
            groups = map(int, fin.readline().split())
            memo = compute_memo(k, groups)

            index = 0
            euros = 0
            ride = 1
            while ride <= R:
                euros += memo[index][0]
                index = (index+memo[index][1]) % len(groups)
                ride += 1

            print('Case #%d: %d' % (n+1, euros))


            #print('Case #%d: %d' % (n+1, euros))
