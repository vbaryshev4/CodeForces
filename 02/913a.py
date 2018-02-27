'''
    http://codeforces.com/problemset/problem/913/A

'''
n = int(input())
m = int(input())

def mod_(m, n):
    if n >= 27:
        return m
    return m%2**(n)

print(mod_(m,n))

# Random attempts
# cases = [[4, 42], [1, 58], [98765432, 23456789]]
# for item in cases:
#     n, m = item[0], item[1]
#     print(mod_(m, n))