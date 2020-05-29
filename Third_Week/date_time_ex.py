import datetime
from datetime import date
from datetime import timedelta

import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

today = date.today()
delta = datetime.timedelta(days = 1)
yesterday = today - delta
tomorrow = today + delta
month_ago = today - 30*delta

date_string = '01/01/25 12:10:03.234567'
date_date = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(yesterday, '\n', today, '\n', tomorrow, '\n', month_ago, '\n')
print(date_date)
