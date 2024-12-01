import lib.AoC_lib as AoC
import operator

@AoC.timer
def first_part(input_file):
    result = 0
    left_list = []
    right_list = []
    
    with open(input_file, 'r') as input:
        for line in input:
            left,right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    left_list.sort()
    right_list.sort()

    diff_list = list(map(operator.sub, left_list, right_list))

    result = sum(abs(number) for number in diff_list)

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    left_list = []
    right_list = []
    
    with open(input_file, 'r') as input:
        for line in input:
            left,right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    left_list.sort()
    right_list.sort()

    for number in left_list:
        score= right_list.count(number)
        result = result + number*score
    return result


if __name__ == '__main__':
    DAY = '01'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))