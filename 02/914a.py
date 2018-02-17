'''
    http://codeforces.com/problemset/problem/914/A
'''

# len_of_values = int(input())
# values = list(map(int, input().split(' ')))

# values = [4, 2]
# values = [1, 2, 4, 8, 16, 32, 64, 576]
values = [-1, -4, -9]

def get_square(value):
    return abs(value)**(1/2)%2

max_v = 0
for v in values:
    # print(v, -get_square(v))
    if get_square(v) != 0:
        max_v = v

print(max_v)
