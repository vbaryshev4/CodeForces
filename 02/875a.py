'''
    http://codeforces.com/problemset/problem/875/A
    Работает, но долго на значении 100000001 
'''

value = int(input())

def display(lst):
    for item in sorted(lst):
        print(item)

def sum_a_string(integer):
    # print(integer)
    return sum([int(d) for d in str(integer)])

def make_all_nine(lenght):
    return '9' * lenght

def d_max(value):
    svalue = str(value)
    value_len = len(svalue)
    first = svalue[0]

    if value_len == 1:
        return value

    if first == '1':
        return sum_a_string(int(make_all_nine(value_len - 1)))

    nines_count = value_len - 1
    first = str(int(first) - 1)
    return sum_a_string(int(first + make_all_nine(nines_count)))

def itter(value):
    count = 0
    possible_digits = []

    if value == 1:
        print(count)
        display(possible_digits)
        return 

    for num in range(value - d_max(value), value - 1):
        result = num + sum_a_string(num)
        if result == value:
            count += 1
            possible_digits.append(num)
    print(count)
    display(possible_digits)

itter(value)

