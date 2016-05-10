import pickle

from pictorial.helpers.decorators import singleton
from pictorial.helpers.objects import Coords


@singleton
class GeoData(object):
    def __init__(self):

        self.filename = "gps_data.txt"

        self.stored_locations = []
        try:
            self.load()
        except:
            self.save()

    def save(self):
        pickle.dump(self.stored_locations, open(self.filename, "wb"))

    def load(self):
        self.stored_locations = pickle.load(open(self.filename, "rb"))

    def add_location(self, lat, long, name):
        self.stored_locations.append(Coords(lat, long, name))

    def get_location(self, lat, long):
        for location in self.stored_locations:
            if lat == location.lat and long == location.long:
                return location.name

        return False
