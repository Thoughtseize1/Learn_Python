from datetime import datetime, timedelta

users_with_correct_dates = [
    {"name": "Brad Pitt", "birthday": '1963-12-18'},
    {"name": "Morgan Freeman", "birthday": '1937-06-01'},
    {"name": "Matt Damon", "birthday": '1970-10-08'},
    {"name": "Michael Caine", "birthday": '1974-06-11'},
    {"name": "Tom Hanks", "birthday": '1956-07-9'},
    {"name": "Gary Oldman", "birthday": '1958-03-21'},
    {"name": "Al Pacino", "birthday": '1940-04-25'},
    {"name": "Bruce Willis", "birthday": '1955-03-19'},
    {"name": "Samuel L. Jackson", "birthday": '1948-12-21'},
    {"name": "Christian Bale", "birthday": '1974-01-30'},
    {"name": "Robert De Niro", "birthday": '1943-08-17'},
    {"name": "Jack Nicholson", "birthday": '1937-04-22'},
    {"name": "Johnny Depp", "birthday": '1963-06-09'},
    {"name": "Harrison Ford", "birthday": '1942-07-13'},
    {"name": "Tom Cruise", "birthday": '1962-07-03'},
]

users = [
    {"name": "Brad Pitt", "birthday": '1963-11-14'},
    {"name": "Morgan Freeman", "birthday": '1937-11-15'},
    {"name": "Matt Damon", "birthday": '1970-11-16'},
    {"name": "Michael Caine", "birthday": '1974-11-17'},
    {"name": "Tom Hanks", "birthday": '1956-11-15'},
    {"name": "Gary Oldman", "birthday": '1958-11-14'},
    {"name": "Al Pacino", "birthday": '1940-11-25'},
    {"name": "Bruce Willis", "birthday": '1955-11-19'},
    {"name": "Samuel L. Jackson", "birthday": '1948-11-18'},
    {"name": "Christian Bale", "birthday": '1974-11-20'},
    {"name": "Robert De Niro", "birthday": '1943-11-20'},
    {"name": "Jack Nicholson", "birthday": '1937-11-22'},
    {"name": "Johnny Depp", "birthday": '1963-11-09'},
    {"name": "Harrison Ford", "birthday": '1942-11-13'},
    {"name": "Tom Cruise", "birthday": '1962-11-03'},
]


'''
#### Начал писать функцию, которая позволяет поймать именинников ещё в этом году.

def get_birthdays_per_week(birthdays):
    today_is = datetime.today()
    birthday_week = today_is + timedelta(days=7)
    print(birthday_week)
    for user in birthdays:
        for i in user.values():
            if i[:1].isdigit():
                date_time_obj = datetime.strptime(i, '%Y-%m-%d')
                print(date_time_obj)
                a = date_time_obj.strftime(str(today_is.year)+'-%m-%d')
                b = date_time_obj = datetime.strptime(a, '%Y-%m-%d')
                print(today_is < b)

'''

day_for_congrats = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}


def find_a_nearby_monday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)


def get_birthdays_per_week(birthdays):
    today_is = datetime.today()
    print(today_is)
    nearby_monday = find_a_nearby_monday(today_is, 0)
    print(nearby_monday)
    birthday_week = nearby_monday + timedelta(days=4)
    print(f'Birthday WEEK  {birthday_week}')
    for user in birthdays:
        for i in user.values():
            # Temporaly remebmer a name of user
            if not i[:1].isdigit():
                user_name = i
            else:
                date_time_obj = datetime.strptime(i, '%Y-%m-%d')
                a = date_time_obj.strftime(str(today_is.year)+'-%m-%d')
                birthday_is_this_year = datetime.strptime(
                    a, '%Y-%m-%d')
                if today_is < birthday_is_this_year < birthday_week:
                    birthday_day = birthday_is_this_year.strftime("%A")
                    if birthday_day in ("Saturday", "Sunday"):
                        day_for_congrats['Monday'].append(user_name)
                    else:
                        day_for_congrats[birthday_day].append(user_name)

    for day, whom_to_congratulate in day_for_congrats.items():
        print(f'{day}: {",".join(whom_to_congratulate)}.')


# date = datetime.strptime(date, '%Y-%m-%d')

get_birthdays_per_week(users)
