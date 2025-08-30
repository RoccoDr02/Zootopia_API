import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        animal_data = json.load(handle)
        return animal_data


def animal_information(animal_data):
    """ Prints the animals in the JSON file """
    for animal in animal_data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Location: {animal['locations'][0]}")
        print(f"Type: {animal['characteristics']['type']}")
        print()


animal_information(load_data("animals_data.json"))
