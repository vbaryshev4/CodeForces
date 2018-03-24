n, k = list(map(int, input().split(' ')))
matrix = []

vip_ctriterea = 0

while n > 0:
	matrix.append(list(input()))
	n -= 1


def find_neighbours(row, index, mask = 'S'):
	left = '-'
	right = '-'

	if index:
		left = row[index-1]

	try:
		right = row[index+1]
	except:
		pass

	if left in mask and right in mask:
		return 2

	if left in mask or right in mask:
		return 1

	else:
		return 0


def find_seat(row):
	global vip_ctriterea
	global k

	for seat in  range(len(row)):
		if k == 0:
			return
		if row[seat] == '.':
			if find_neighbours(row, seat) == vip_ctriterea:
				row[seat] = 'x'
				k -= 1

def display(matrix):
	for row in matrix:
		print(''.join(row))


def itter_matrix(matrix):
	global k
	global vip_ctriterea

	while k != 0:
		for row in matrix:
			find_seat(row)
		vip_ctriterea += 1

	neighbours = 0
	for row in matrix:
		i = 0
		while i < len(row):
			if row[i] == 'S':
				neighbours += find_neighbours(row, i, 'SPx')
			i += 1

	print(neighbours)
	display(matrix)


itter_matrix(matrix)