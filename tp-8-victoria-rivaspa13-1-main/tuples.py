def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])


def create_record(azara_record, rui_record):
    treasure_name, treasure_coordinate = azara_record
    location_name, location_coordinate, quadrant = rui_record

    formatted_coordinate = convert_coordinate(treasure_coordinate)

    if formatted_coordinate == location_coordinate:
        return (treasure_name, treasure_coordinate, location_name, location_coordinate, quadrant)
    else:
        return "not a match"