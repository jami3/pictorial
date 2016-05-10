import os


def convert_gps_coords(dms, hemisphere):
    precision = 3
    degrees = convert_ratio(dms[0])
    minutes = convert_ratio(dms[1])
    seconds = convert_ratio(dms[2])

    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)

    if 'W' in hemisphere or 'S' in hemisphere:
        decimal_degrees = -decimal_degrees

    return round(decimal_degrees, precision)


def convert_ratio(ratio):
    if '/' in str(ratio):
        ratio_split = str(ratio).split("/")
        ratio_as_float = float(ratio_split[0]) / float(ratio_split[1])
    else:
        ratio_as_float = float(ratio.num)

    return ratio_as_float


def create_directory(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
