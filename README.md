Call the add_time function (2 arguments + 1 optionnale) to return the correct time format after adding minutes.
add_time(start, duration, day)

start: Type = String ; Time to start the minute addition (format "h:min XX")
durations: Type = String ; Time to be added to the starting time (format "h:min)
day: Type : String : Day of the week (case unsensitive)


Use exemples:

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)
