import calendar
import schedule
import time
#c = calendar.TextCalendar(calendar.MONDAY)
#c.prmonth(2020,9)
#print(calendar.month(2020,9))
#day_of_the_week = calendar.weekday(2020,9,12)
#print(day_of_the_week)

def store_reminder_of_date():
    prompt_date = input('please enter the date corresponding to reminder you\'d like to store,please enter\n year,month,date\nfor example 22nd september 2020 would be 2020,9,22:\n')
    year = str(prompt_date).split(',')[0]
    month = str(prompt_date).split(',')[1]
    day = str(prompt_date).split(',')[2]
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    day_of_week = calendar.weekday(year_int,month_int,day_int)
    week_day = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print(f" your reminder will fall on a '{week_day[day_of_week]}'" )

def schedule_reminder():
    reminder = input('what would you like to be reminded of this week?')
    reminder_question(reminder)

def reminder_question(reminder):
    print(reminder)

#schedule.every(5).seconds.do(schedule_reminder)
#schedule.every().monday.do(schedule_reminder)
#schedule.every().wednesday.at("13.12").do(schedule_reminder)

while True:
    schedule.run_pending()
    time.sleep(1) #delays time of execution and the while true loop means message repeats


