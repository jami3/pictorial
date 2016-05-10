import os.path
import threading

import shutil
from tqdm import tqdm

from pictorial.geo_data import GeoData
from pictorial.helpers.functions import create_directory
from pictorial.image import Image
from pictorial.location import get_geo_location


class PhotoSorter():
    image_files = []

    def __init__(self, root_directory, target_directory):
        self.root_directory = root_directory
        self.target_directory = target_directory
        self.geo_data = GeoData()
        self.images = []

    def build_image_objects(self):
        os.path.walk(self.root_directory, self._get_images, 0)
        print "\nGenerating images"
        for file in tqdm(self.image_files):
            threading.Thread(target=self.images.append(Image(file)))

    def generate_file_names(self):
        print "\nGenerating file names"
        unknown_files_count = 0
        for image in tqdm(self.images):
            name = image.generate_file_name()
            if name == '':
                unknown_files_count = unknown_files_count + 1
                image.file_name = "image_" + str(unknown_files_count)

        self.geo_data.save()

    def move_images_to_new_directory(self):
        print "\nCopying images"
        for image in tqdm(self.images):
            if image.has_date_info:
                save_directory = self.target_directory + "/" + image.date.year + "/" + image.date.month_name + "/"
            elif image.has_gps_info:
                save_directory = self.target_directory + "/" + image.location.street
            else:
                save_directory = self.target_directory + "/" + "miscellaneous/"

            create_directory(save_directory)
            shutil.copy(image.path, save_directory + image.file_name)

    def sort_images(self):
        self.build_image_objects()
        self.generate_file_names()
        self.move_images_to_new_directory()

    def _get_images(self, x, dir_name, files):
        for file in files:
            if "jpg" in file.lower():
                self.image_files.append(dir_name + '/' + file)


if __name__ == "__main__":
    sorter = PhotoSorter("/home/jamiemirl/pictures_recovered/001", "/home/jamiemirl/pictures/sorted_photos")
    sorter.build_image_objects()
    sorter.generate_file_names()
    sorter.move_images_to_new_directory()

    print "\nGeocoder calls", get_geo_location.calls
