from datetime import datetime


def current_season(current_month):
    if current_month in range(4, 10):
        season = str("Summer")
    else:
        season = str("Winter")
    return season


currentMonth = datetime.today().month
print(current_season(currentMonth))
