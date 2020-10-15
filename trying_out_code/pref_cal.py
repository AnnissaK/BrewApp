import datetime
import calendar
def get_day_of_week():
    index_of_week =datetime.datetime.today()
    weekday = calendar.day_name[index_of_week.weekday()]
    print(weekday)
    

get_day_of_week()