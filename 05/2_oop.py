class Calendar(object):
    def __init__(self):
        self.calendar = {}

    def __get_time(self, string):
        result = string.split(':')
        result = int(result[0])*60 + int(result[1])
        return result

    def appoint(self, item):
        day = item[0]
        start_time = self.__get_time(item[1])
        end_time = start_time + int(item[2])
        count_participants = item[3]
        names = item[4:]
        invalid_names = []

        can_create = True    

        for name in names:
            person_calendar = self.calendar.get(name, {})
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
                self.calendar[name] = self.calendar.get(name, {})
                self.calendar[name][day] = self.calendar[name].get(day, [])
                self.calendar[name][day].append([start_time, end_time, names, item[1]])
            print('OK')

        else:
            print('FAIL')
            print(' '.join(invalid_names) + ' ')

    def display(self, item):
        day = item[0]
        name = item[1]

        person_calendar = self.calendar.get(name)

        if not person_calendar:
            return

        appointments = person_calendar.get(day)

        if not appointments:
            return

        for appointment in appointments:
            start, end, names, time = appointment
            print(' '.join([time, str(end - start)] + names))


class Data(object):
    def __init__(self):
        self.data = []
        
requests = int(input())
d = Data()

i = 0
while i != requests:
    values = list(map(str, input().split(' ')))
    d.data.append(values)
    i += 1

def itter(cls):
    cal = Calendar()
    for item in cls.data:
        if item[0] == 'APPOINT':
            cal.appoint(item[1:])
        elif item[0] == 'PRINT':
            cal.display(item[1:])

itter(d)


# Ввод
# 6
# APPOINT 1 12:30 30 2 andrey alex
# APPOINT 1 12:00 30 2 alex sergey
# APPOINT 1 12:59 60 2 alex andrey
# PRINT 1 andrey
# PRINT 1 sergey
# PRINT 2 alex

# Вывод
# OK
# OK
# FAIL
# alex andrey 
# 12:30 30 andrey alex
# 12:00 30 alex sergey