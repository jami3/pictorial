from pictorial.data_structures import months_short_name, months_long_name


class Coords(object):
    def __init__(self, lat, long, name):
        self.lat = lat
        self.long = long
        self.name = name


class Date(object):
    def __init__(self, date_time):
        date_time = str(date_time.values).encode("utf-8")
        self.date_items = date_time.split(" ")
        self.date_list = self.date_items[0].split(":")

        self.year = self.date_list[0]
        self.day = self.date_list[2]
        self.month = self.date_list[1]
        self.date = self.year + self.day + self.month

        self.month_name_short = months_short_name[self.month]
        self.month_name = months_long_name[self.month]

        self.time_list = self.date_items[1].split(":")
        self.hour = self.time_list[0]
        self.minute = self.time_list[1]
        self.seconds = self.time_list[2]
        self.time = self.hour + self.minute + self.seconds
