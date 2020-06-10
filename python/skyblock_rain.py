import time


__credits__ = ["Men2Martyrs", "LinJay"]

"""
Notes:
       |back_cycle() and prev_rain() are for debugging purposes.
"""

months = [
    "Early Spring", "Spring", "Late Spring",
    "Early Summer", "Summer", "Late Summer",
    "Early Autumn", "Autumn", "Late Autumn",
    "Early Winter", "Winter", "Late Winter",
]

days = [
    "1st", "2nd", "3rd", "4th", "5th", "6th", "7th",
    "8th", "9th", "10th", "11th", "12th", "13th", "14th",
    "15th", "16th", "17th", "18th", "19th", "20th", "21st",
    "22nd", "23rd", "24th", "25th", "26th", "27th", "28th",
    "29th", "30th", "31st",
]

hours = [
    "12am", "1am", "2am", "3am", "4am", "5am",
    "6am", "7am", "8am", "9am", "10am", "11am",
    "12pm", "1pm", "2pm", "3pm", "4pm", "5pm",
    "6pm", "7pm", "8pm", "9pm", "10pm", "11pm",
]


def cycle(lst, item): # only cycles one instance
    ind = lst.index(item)
    try:
        return lst[ind+1], False
    except IndexError:
        return lst[0], True # True if overflow


def back_cycle(lst, item):
    ind = lst.index(item)
    if ind != 0:
        return lst[ind-1], False
    else:
        return lst[-1], True


def next_rain(date):
    # date = [months, days, hours]
    h = date[2]
    nh, over = cycle(hours, h)
    if over:
        nd, over2 = cycle(days, date[1])
        if over2:
            nm, over3 = cycle(months, date[0])
            if over3:
                new_year = True
    try:
        nd
    except:
        nd = date[1]
    for x in "x"*4:
        nd, over = cycle(days, nd)
        if over:
            nm, over2 = cycle(months, date[0])
            if over2:
                new_year = True
    try:
        nm
    except:
        nm = date[0]
    try:
        new_year
    except:
        new_year = False
    return [nm, nd, nh], new_year


def prev_rain(date):
    h = date[2]
    nh, over = back_cycle(hours, h)
    if over:
        nd, over2 = back_cycle(days, date[1])
        if over2:
            nm, over3 = back_cycle(months, date[0])
            if over3:
                new_year = True
    try:
        nd
    except:
        nd = date[1]
    for x in "x"*4:
        nd, over = back_cycle(days, nd)
        if over:
            nm, over2 = back_cycle(months, date[0])
            if over2:
                new_year = True
    try:
        nm
    except:
        nm = date[0]
    try:
        new_year
    except:
        new_year = False
    return [nm, nd, nh], new_year


def get_start(year): # year is the start of the year
    year_length = 446400
    rain_distance = 4850

    # current = year0 + (year_length * year)
    events = ((year_length * year) // rain_distance) - 2
    date = ['Early Spring', '4th', '5am'] # year 0 start date

    y = 0
    for i in range(events):
        dup = 0
        date, new_year = next_rain(date)
        if new_year and dup == 0:
            y += 1
            dup = 1
    loop = True
    while loop:
        if date[1] not in ["1st", "2nd", "3rd", "4th"] and date[0] != "Early Spring":
            if date[0] !=  "Late Winter":
                date,o = prev_rain(date)
            else:
                date,o = next_rain(date)
        else:
            loop = False

    return date, y, events


def to_hms(dist):
    h, left = int(dist) // 3600, int(dist) % 3600
    m, left = left // 60, left % 60
    s = left

    return "in {} hrs, {} mins and {} seconds.".format(h, m, s)


def main():
    #"""
    try:
        # year shown in skyblock menu refers to the end of the year
        current_year = int(input("Enter the year shown at the top of your calendar: "))
    except ValueError:
        print("Invalid year entered.")
        return

    start,events = get_start(current_year)[0::2]
    year0 = 1560272100
    rain_distance = 4850
    event_epoch = year0 + (4850 * events) - 424400
    instance_epoch = int(time.time())

    #"""
    rain_dates = {}
    date = start
    loop = True
    rain_dates[tuple(date)] = event_epoch
    e = 0
    while loop:
        e += 1
        date,over = next_rain(date)
        rain_dates[tuple(date)] = event_epoch + (rain_distance * e)
        if over:
            loop = False
    txt = ""
    for date in rain_dates:
        distance = rain_dates[tuple(date)] - instance_epoch
        if distance < 0:
            remaining = "Already happened."
        else:
            remaining = to_hms(distance)

        t = "{}, {} at {}\t({})\n".format(
            *date,
            remaining,
        )
        txt += t
    txt = txt[:-1]
    print(txt + "\n\n")


while __name__ == "__main__":
    main()
