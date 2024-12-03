import lib.AoC_lib as AoC


@AoC.timer
def first_part(input_file):
    result = 0
    
    with open(input_file, 'r') as input:
        for line in input:
            report = [int(x) for x in line.strip().split()]
            diff_list = [j-i for i, j in zip(report[:-1], report[1:])]
            
            if abs(max(diff_list)) > 3 or abs(min(diff_list)) > 3:
                continue
            if diff_list.count(0) > 0:
                continue
            
            if diff_list[0] > 0:
                flag = any(x < 0 for x in diff_list)
                if flag:
                    continue
            elif diff_list[0] < 0:
                flag = any(x > 0 for x in diff_list)
                if flag:
                    continue

            result = result + 1

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    

    return result


if __name__ == '__main__':
    DAY = ''

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))