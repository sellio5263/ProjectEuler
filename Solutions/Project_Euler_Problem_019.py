# Data formed as [year, month, day of month, day of week] (day of week is Sunday-0, Monday-1...)
startDate = [1900,1,1,2]
import time

def compute():
    sum_first_sundays = 0
    
    date = startDate

    while date[0] != 2001:
        # If we're into the twentieth century so we should be counting and we meet the criteria
        if (date[0] >= 1901) and (date[3] == 1 and date[2] == 1):
            sum_first_sundays += 1
        # Move to the next Day
        date = next_day(date)
        
    return str(sum_first_sundays)

def next_day(day):
    #Update Day of the Week
    day[3] += 1
    if (day[3] == 8):
        day[3] = 1

    #Update Calendar Date
    num_days = get_num_days(day[1], day[0])

    day[2] += 1
    if (day[2] == num_days +1): #Reset Day of Month
        day[2] = 1
        day[1] += 1
        if (day[1] == 13): #Reset Month
            day[1] = 1
            day[0] += 1

    return day

def get_num_days(month, year):
    # List of number of days in the month
    num_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_days = num_days_list[month-1]

    # Add leap day if it's a leap year and month is feburary
    if(month == 2 and is_leap_year(year)):
        num_days += 1

    return num_days

def is_leap_year(year):
    # Leap years are every 4 years except for centuries when it's only if they're divisible by 400
    if year%100==0:
        return year%400 == 0
    else:
        return year%4 == 0
    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

