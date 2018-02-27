'''
    http://codeforces.com/problemset/problem/914/A
'''

len_of_values = int(input())
values = list(map(int, input().split(' ')))

def get_square(values):
    maximum = -1000000
    for value in values:
        # print(value, (abs(value**(1/2)))%2)
        if value < 0 and (abs(value**(1/2)) % 2) != 0.0 and maximum < value:
                maximum = value
        elif value > 0 and (abs(value**(1/2)) % 1) != 0.0 and maximum < value:
            maximum = value
    return maximum

print(get_square(values))

# 4 2
# 1 2 4 8 16 32 64 576
# -1 -4 -9
# 994009 992109

# wrong answer 1st numbers differ - expected: '992109', found: '994009'