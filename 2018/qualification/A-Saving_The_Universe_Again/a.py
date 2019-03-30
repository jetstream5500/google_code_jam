def compute_damages(program):
    damage_list = []
    total = 0
    multiple = 1
    for letter in program:
        if letter == 'C':
            multiple*=2
            damage_list.append(0)
        else:
            total += multiple
            damage_list.append(multiple)

    return (total, damage_list)


if __name__ == '__main__':
    num_test_cases = int(raw_input())
    for n in range(num_test_cases):
        test_case = raw_input().split()
        shield = int(test_case[0])
        program = test_case[1]
        total, damage_list = compute_damages(program)
        damage = sum(damage_list)

        solved = False
        count = 0
        for i in range(len(damage_list)-1, -1, -1):
            if damage <= shield:
                solved = True
                break

            if damage_list[i] == 0:
                for j in range(i+1, len(damage_list)):
                    if damage_list[j] != 0:
                        count += 1
                        temp = damage_list[i]
                        damage_list[i] = damage_list[j]/2
                        damage -= damage_list[j]/2
                        damage_list[j] = temp
                        i+=1
                        #print(damage_list)
                    else:
                        break

                    if damage <= shield:
                        solved = True
                        break

        if solved:
            print('Case #%d: %d' % (n+1, count))
        else:
            print('Case #%d: IMPOSSIBLE' % (n+1))
