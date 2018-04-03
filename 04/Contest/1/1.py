servers_count = int(input())
data = []

i = 0
while i != servers_count:
	values = list(map(int, input().split(' ')))
	data.append(values)
	i += 1

def count_Omega(data):
	result = 0
	for server in data:
		result += server[0]*server[1]
	return result

Omega = count_Omega(data)

def itter(data):
	result = 0
	for server in data:
		result = server[0] * server[1]/Omega
		print(result)

itter(data)