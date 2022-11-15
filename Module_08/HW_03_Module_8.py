from datetime import datetime


def get_str_date(date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f%z')
    return date_time_obj.strftime('%A %d %B %Y')


print(get_str_date('2021-05-27 17:08:34.149Z'))
