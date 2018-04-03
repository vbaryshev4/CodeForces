add, supply, day = list(map(int, input().split(' ')))

was_read = 1
days = 0
books = supply

def readable():
    global add
    global supply
    global day
    global was_read 
  
    if day < 6:
        supply += add

    supply = supply - was_read

    was_read += 1
    day += 1
    if day == 8:
        day = 1

    return supply >= 0

while readable():
    days += 1

print(days)