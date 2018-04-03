requests = int(input())


data = []

i = 0
while i != requests:
    values = list(map(str, input().split(' ')))
    data.append(values)
    i += 1

calendar = {}

def get_time(string):
    result = string.split(':')
    result = int(result[0])*60 + int(result[1])
    return result

def appoint(item):
    day = item[0]
    start_time = get_time(item[1])
    end_time = start_time + int(item[2])
    count_participants = item[3]
    names = item[4:]
    invalid_names = []

    can_create = True    

    for name in names:
        person_calendar = calendar.get(name, {})
        appointments = person_calendar.get(day, [])

        for appointment in appointments:
            a_start, a_end, appointment_names = appointment[:3]
            s1 = set(range(start_time, end_time))
            s2 = set(range(a_start, a_end))

            if bool(s1.intersection(s2)):
                can_create = False
                invalid_names.append(name)
                break

    if can_create == True:
        for name in names:
            calendar[name] = calendar.get(name, {})
            calendar[name][day] = calendar[name].get(day, [])
            calendar[name][day].append([start_time, end_time, names, item[1]])
        print('OK')

    else:
        print('FAIL')
        print(' '.join(invalid_names) + ' ')

def display(item):
    day = item[0]
    name = item[1]

    person_calendar = calendar.get(name)

    if not person_calendar:
        return

    appointments = person_calendar.get(day)

    if not appointments:
        return

    # [750, 780, ['andrey', 'alex'], '12:30']
    for appointment in appointments:
        start, end, names, time = appointment
        print(' '.join([time, str(end - start)] + names))


def itter(data):
    for item in data:
        if item[0] == 'APPOINT':
            appoint(item[1:])
        elif item[0] == 'PRINT':
            display(item[1:])

itter(data)