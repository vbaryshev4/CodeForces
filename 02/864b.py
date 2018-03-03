'''
	http://codeforces.com/problemset/problem/864/B
	DONE
'''

value = int(input())
string = input()

def count(result): 
	print(len(result) and max(map(len, result)))

def itter(string):
	result = []
	small = set()
	for s in string:
		if s.islower():
			small.add(s)
		else:
			if len(small):
				result.append(small)
			small = set()
	if len(small):
		result.append(small)
	count(result)

itter(string)