'''
    http://codeforces.com/problemset/problem/875/A
    Работает, но долго на значении 100000001 
'''

value = int(input())

def display(lst):
    for item in sorted(lst):
        print(item)

def sum_a_string(digit):
    result = 0
    for i in str(digit):
        result+=int(i)
    return result

def get_sum(value):
    count = 0
    possible_digits = []
    for num in range(int(value/2),value):
        result = num + sum_a_string(num)
        if result == value:
            count += 1
            possible_digits.append(num)
    print(count)
    display(possible_digits)

get_sum(value)