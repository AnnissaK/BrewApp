import datetime
import calendar
def week_day():
    index_of_week =datetime.datetime.today()
    week_day = calendar.day_name[index_of_week.weekday()]
    return week_day
