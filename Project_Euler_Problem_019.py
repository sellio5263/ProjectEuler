startDate = [1900,1,1,2]

def compute():
    sumFirstSundays = 0
    
    date = startDate

    while date[0] != 2001:
        if date[0] >= 1901:
            if date[3] == 1 and date[2] == 1:
                sumFirstSundays += 1
        date = nextDay(date)
        
    return str(sumFirstSundays)

def nextDay(day):
    #Update Day of the Week
    day[3] += 1
    if (day[3] == 8):
        day[3] = 1

    #Update Calendar Date
    numDays = getNumDays(day[1], day[0])

    day[2] += 1
    if (day[2] == numDays +1): #Reset Day of Month
        day[2] = 1
        day[1] += 1
        if (day[1] == 13): #Reset Month
            day[1] = 1
            day[0] += 1

    return day

def getNumDays(month, year):
    numDaysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    numDays = numDaysList[month-1]

    if(month == 2 and isLeapYear(year)):
        numDays += 1

    return numDays

def isLeapYear(year):
    if year%100==0:
        return year%400 == 0
    else:
        return year%4 == 0
    
if __name__ == "__main__":
    print(compute())

