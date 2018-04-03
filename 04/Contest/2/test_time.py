def get_time(string):
    result = string.split(':')
    result = int(result[0])*60 + int(result[1])
    return result

time_lst = []
for hour in range(8,22):
	for minute in range(00,60):
		print(hour, minute)

# for time in time_lst:

