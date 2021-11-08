import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, flat_type, storey_range, sqm, remaining_lease):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = flat_type
    x[1] = storey_range
    x[2] = sqm
    x[3] = remaining_lease
    if loc_index >= 0:
        x[loc_index] = 1

    return str(round(__model.predict([x])[0], 2))


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifact...start")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
    with open("./artifacts/hdb_resale_price.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())
    # print(get_estimated_price("ANG MOH KIO",3,5,60,50))
