def pad_result(num):
    num_str = str(num)
    return '0'*(4-len(num_str)) + num_str

if __name__ == '__main__':
    with open('C-large-practice.in.txt') as fin:
        phrase = 'welcome to code jam'
        num_test_cases = int(fin.readline())
        for n in range(num_test_cases):
            line = fin.readline()
            table = [[0]*len(line) for letter in phrase]

            for i,c_base in enumerate(phrase):
                for j,c in enumerate(line):
                    if c_base == c:
                        if i == 0:
                            sum = 1
                            if j > 0:
                                sum += table[i][j-1]
                            table[i][j] = sum  % 10000
                        else:
                            sum = 0
                            if j > 0:
                                sum += table[i][j-1]
                                if i > 0:
                                    sum += table[i-1][j-1]
                            table[i][j] = sum  % 10000
                    else:
                        sum = 0
                        if j > 0:
                            sum += table[i][j-1]
                        table[i][j] = sum % 10000

            print('Case #' + str(n+1) + ': ' + pad_result(table[-1][-1]))
