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
        for key, value in animal.items():
            if key == "locations":
                print("Location: " + value[0])
            if key == "characteristics":
                for characteristic, value in value.items():
                    if characteristic == "diet":
                        print("Diet: " + value)
                    if characteristic == "type":
                        print("Type: " + value)
        print()


animal_information(load_data("animals_data.json"))
