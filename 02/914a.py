'''
    http://codeforces.com/problemset/problem/914/A
    DONE
'''


len_of_values = int(input())
values = list(map(int, input().split(' ')))


def get_square(values):
    maximum = -1000000
    for value in values:
        if value < 0 and (abs(value**(1/2)) % 2) != 0.0 and maximum < value:
                maximum = value
        elif value > 0 and (abs(value**(1/2)) % 1) != 0.0 and maximum < value:
            maximum = value
    return maximum

print(get_square(values))