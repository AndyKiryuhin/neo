"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.
    """
    neos = []
    with open(neo_csv_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            neo = NearEarthObject(row[3], name=row[4], diameter=row[15], hazardous=True if row[7]=="Y" else False)
            neos.append(neo)
    return neos
    """
    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.

#NEO_DB = load_neos(r"C:\Users\SurfaceUser\OneDrive\Dev\Udacity\neo\data\neos.csv")
NEO_DB = load_neos(r"./data/neos.csv")

def load_approaches(cad_json_path):

    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    approaches = []
    with open(cad_json_path) as jsonfile:
        data = json.load(jsonfile)
        for row in data["data"]:
            approache = CloseApproach(row[0], time=row[3], distance=row[4], velocity=row[7])
            approaches.append(approache)
    return approaches

#APPROACH_DB = load_approaches(r"C:\Users\SurfaceUser\OneDrive\Dev\Udacity\neo\data\cad.json")
APPROACH_DB = load_approaches(r"./data/cad.json")