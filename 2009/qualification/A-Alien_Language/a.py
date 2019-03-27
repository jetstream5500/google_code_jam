
if __name__ == '__main__':
    with open('A-large-practice.in.txt', 'r') as fin:
        vals = map(int, fin.readline().split())
        word_length = vals[0]
        dictionary_length = vals[1]
        num_test_cases = vals[2]

        dictionary = []
        for i in range(dictionary_length):
            word = fin.readline().rstrip('\n')
            dictionary.append(word)

        for n in range(num_test_cases):
            code = fin.readline().rstrip('\n')
            options = []
            while len(code) > 0:
                if code.startswith('('):
                    options.append( code[code.index('(')+1:code.index(')')] )
                    code = code[code.index(')')+1:]
                else:
                    options.append( code[0] )
                    code = code[1:]

            count = 0

            for word in dictionary:
                broken = False
                for i, c in enumerate(word):
                    if c not in options[i]:
                        broken = True
                        break
                if not broken:
                    count+=1

            print('Case #%d: %d' % (n+1, count))
