def add_time(start, duration,day=' '):
    indicator = start[start.find(' ')+1:]
    newora = int(start[:start.find(':')]) + int(duration[:duration.find(':')])
    newlepta = int(start[start.find(':')+1:start.find(' ')]) + int(duration[duration.find(':')+1:])
    if(newlepta >= 60):
        newora += 1
        newlepta = newlepta - 60
    if(newlepta < 10):
        newlepta = '0{}'.format(newlepta)
    days = 0
    weekdays = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    pastindicator = indicator
    while(newora >= 12):
        print(newora,indicator,pastindicator,days)
        if(indicator == 'AM'):
            pastindicator = indicator
            indicator = 'PM'
        else:
            pastindicator = indicator
            indicator = 'AM'
        if(pastindicator == 'PM' and indicator == 'AM'):
            days += 1
        if(newora == 12 and (indicator == 'PM' or indicator == 'AM')):
            break  
        newora -= 12
    if(day != ' '):
        day = day.upper()
        temp = weekdays.index(day)
        for j in range(days):
            temp += 1
            if(temp >= len(weekdays)):
                temp = 0
        Day = weekdays[temp][1:].lower()
        day = weekdays[temp][0] + Day
        if(days == 0):
            new_time = f'{newora}:{newlepta} {indicator}, {day}'
        if(days == 1):
            new_time = f'{newora}:{newlepta} {indicator}, {day} (next day)'
        if(days > 1):
            new_time = f'{newora}:{newlepta} {indicator}, {day} ({days} days later)'
    else:
        if(days == 0):
            new_time = f'{newora}:{newlepta} {indicator}'
        if(days == 1):
            new_time = f'{newora}:{newlepta} {indicator} (next day)'
        if(days > 1):
            new_time = f'{newora}:{newlepta} {indicator} ({days} days later)'
    
    return new_time

time = add_time('11:59 PM','24:05')
print(time)
quit()