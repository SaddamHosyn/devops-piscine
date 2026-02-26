# Mapping from number to day
number_to_day = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# Reverse mapping from day to number
day_to_num = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

def day_from_number(day_number):
    return number_to_day.get(day_number, None)

def day_to_number(day):
    return day_to_num.get(day, None)
