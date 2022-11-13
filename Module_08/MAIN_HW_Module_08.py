from datetime import datetime, timedelta, date


def find_a_nearby_monday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)


def get_birthdays_per_week(birthdays):
    today_is = datetime.today()
    nearby_monday = find_a_nearby_monday(today_is, 0)
    end_of_birthday_week = nearby_monday + timedelta(days=4)
    for user in birthdays:
        for i in user.values():
            # Temporaly remebmer a name of user
            if type(i) != datetime:
                user_name = i
            else:
                birthday_is_this_year = i.replace(year=today_is.year)
                if today_is < birthday_is_this_year < end_of_birthday_week:
                    birthday_day = birthday_is_this_year.strftime("%A")
                    if birthday_day in ("Saturday", "Sunday"):
                        day_for_congrats['Monday'].append(user_name)
                    else:
                        day_for_congrats[birthday_day].append(user_name)

    for day, whom_to_congratulate in day_for_congrats.items():
        print(f'{day}: {", ".join(whom_to_congratulate)}.')


users = [
    {"name": "Brad Pitt", "birthday": datetime(1963, 11, 14)},
    {"name": "Morgan Freeman", "birthday": datetime(1937, 11, 15)},
    {"name": "Matt Damon", "birthday": datetime(1970, 11, 16)},
    {"name": "Michael Caine", "birthday": datetime(1974, 11, 17)},
    {"name": "Tom Hanks", "birthday": datetime(1956, 11, 15)},
    {"name": "Gary Oldman", "birthday": datetime(1958, 11, 14)},
    {"name": "Al Pacino", "birthday": datetime(1940, 11, 25)},
    {"name": "Bruce Willis", "birthday": datetime(1955, 11, 19)},
    {"name": "Samuel L. Jackson", "birthday": datetime(1948, 11, 18)},
    {"name": "Christian Bale", "birthday": datetime(1974, 11, 20)},
    {"name": "Robert De Niro", "birthday": datetime(1943, 11, 20)},
    {"name": "Jack Nicholson", "birthday": datetime(1937, 11, 22)},
    {"name": "Johnny Depp", "birthday": datetime(1964, 11, 22)},
    {"name": "Harrison Ford", "birthday": datetime(1942, 11, 3)},
    {"name": "Tom Cruise", "birthday": datetime(1962, 11, 13)}
]


day_for_congrats = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}

get_birthdays_per_week(users)
