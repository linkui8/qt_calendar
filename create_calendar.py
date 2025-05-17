import sqlite3


# Подключение к БД
conn = sqlite3.connect('calendar.db')

# Создание курсора
curs = conn.cursor()
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days30 = [4, 6, 9, 11]
date = 1
month = 1
x = 2
for i in range(365):
    query_str = f"insert into dates1(date, month, day) values('{date}', '{month}', '{days[x]}');"
    query = curs.execute(query_str)
    if date == 30 and (month in days30):
        month += 1
        date = 0
    elif date == 31:
        month += 1
        date = 0
    elif date == 28 and month == 2:
        month += 1
        date = 0
    date += 1
    if x == 6:
        x = 0
    else:
        x += 1

conn.commit()
conn.close()