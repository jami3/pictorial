import re
from geopy import Nominatim

from pictorial.helpers.decorators import counted


@counted
def get_geo_location(lat, long):
    geo = Nominatim()
    string = "{0} , {1}".format(lat, long)
    geo_location = geo.reverse(string, timeout=5)

    return geo_location.address


class Location(object):
    def __init__(self, location):
        location = location.encode("utf-8")
        location = re.sub(" \d+", " ", str(location))
        self.set = str(location).split(" ")
        self.street = str(self.set[0]).replace(" ", "_")
        self.locale = str(self.set[1]).replace(" ", "_")
        self.town = str(self.set[2]).replace(" ", "_")
        self.province = str(self.set[3]).replace(" ", "_")
