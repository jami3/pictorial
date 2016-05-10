import exifread

from pictorial.geo_data import GeoData
from pictorial.helpers.functions import convert_gps_coords
from pictorial.helpers.objects import Date
from pictorial.location import get_geo_location, Location


class Image(object):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.exif_data = exifread.process_file(self.file)
        self.geo_data = GeoData()
        self.file.close()
        self._set_geo_coordinates()

    def _get_image_location(self):
        if self.has_gps_info == True:
            lat = convert_gps_coords(self.latitude.values, self.latitude_ref.values)
            long = convert_gps_coords(self.longitude.values, self.longitude_ref.values)
            if not self._in_stored_locations(lat, long):
                self.location_name = get_geo_location(lat, long)
                self.location = Location(self.location_name)
                self.geo_data.add_location(lat, long, self.location_name)
        else:
            self.location = False

    def _in_stored_locations(self, lat, long):
        location = self.geo_data.get_location(lat, long)
        if location == False:
            return False
        else:
            self.location = Location(location)
            return True

    def _set_geo_coordinates(self):
        if 'GPS GPSLongitude' in self.exif_data.keys() and 'GPS GPSLatitude' in self.exif_data.keys():
            self.longitude = self.exif_data['GPS GPSLongitude']
            self.longitude_ref = self.exif_data['GPS GPSLongitudeRef']
            self.latitude = self.exif_data['GPS GPSLatitude']
            self.latitude_ref = self.exif_data['GPS GPSLatitudeRef']
            self.has_gps_info = True
        else:
            self.has_gps_info = False

    def _set_date_time(self):
        if 'Image DateTime' in self.exif_data.keys():
            self.has_date_info = True
            self.timestamp = self.exif_data['Image DateTime']
            self.date = Date(self.timestamp)
        else:
            self.has_date_info = False

    def generate_file_name(self):
        self._set_date_time()
        self._get_image_location()

        self.file_name = ''

        if self.has_gps_info:
            self.file_name.append(self.location.street.replace(",", "") + "_" + self.location.town.replace(",", ""))

        if self.has_date_info:
            self.file_name.append(self.date.date + "_" + self.date.time + ".jpg")

        if self.file_name != '':
            self.file_name.append('.jpg')

        return self.file_name
