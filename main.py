def add_time(start, duration, day=None):
    #separate starting time (ok)
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_lowcase = list(map(lambda x: x.lower(), week))
    start_hours = int(start.split(":")[0])
    
    start_minutes = int(start.split(':')[1].split(" ")[0])
    
    start_moment = start[-2:]

    #separate starting time
    duration_hours = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]
    #counter
    days_count = 0

    #counting minutes
    for i in range(int(duration_minutes)):
        start_minutes += 1
        if start_minutes >= 60:
            start_minutes = 0
            start_hours += 1
            if start_hours == 12:
                start_hours = 0
                if start_moment == "AM":
                    start_moment = "PM"
                elif start_moment == "PM":
                    start_moment = "AM"
                    days_count += 1
    #counting hours
    for j in range(int(duration_hours)):
        start_hours += 1
        if start_hours == 12:
            start_hours = 0
            if start_moment == "AM":
                    start_moment = "PM"
            elif start_moment == "PM":
                start_moment = "AM"
                days_count += 1

    if len(str(start_minutes)) == 1 :
        start_minutes = "0" + str(start_minutes)

 #Hour format correction   
    if start_hours == 0:
        start_hours = 12

#if day specified
    if type(day)==str and day.lower() in week_lowcase:
        #Find new week indices considering day shift
        new_day_index = (week_lowcase.index(day.lower()) + days_count) % 7
        new_day= week[new_day_index]
        if days_count == 0:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment + ", " + new_day
        elif days_count == 1:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment + ", " + new_day + " (next day)"
        elif days_count > 1:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment + ", " + new_day + " (" + str(days_count) + " days later)"
#Day not specified
    else:   
    #Formatting new_time depending of the day count
        if days_count == 0:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment
        elif days_count == 1:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment + " (next day)"
        elif days_count > 1:
            new_time = str(start_hours) + ":" + str(start_minutes) + " " + start_moment + " (" + str(days_count) + " days later)"
    return new_time 

print(add_time('3:30 PM', '2:12', 'Monday'))

