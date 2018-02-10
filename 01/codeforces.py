rows, kg_to_buy = list(map(int, input().split(' ')))

def low_price(price, kg_price):
	return price/kg_price*kg_to_buy

results = []
while rows:
	price, kg_price = list(map(int, input().split(' ')))
	results.append(low_price(price, kg_price))
	rows -= 1

print(min(results))
