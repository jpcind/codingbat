def alarm_clock(day, vacation):
    weekend = [0,6]
    weekday = []
    for i in range(1,6):
        weekday.append(i)

    if vacation:
        if day in weekend:
            return "off"
        if day in weekday:
            return "10:00"
    else:
        if day in weekday:
            return "7:00"
        if day in weekend:
            return "10:00"
