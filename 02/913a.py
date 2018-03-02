'''
	http://codeforces.com/problemset/problem/913/A
	DONE
'''
n = int(input())
m = int(input())

def mod_(m, n):
    if n >= 27:
        return m
    return m%2**(n)

print(mod_(m,n))