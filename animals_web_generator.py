import json

from pygame.examples.midi import output_main


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        animal_data = json.load(handle)
        return animal_data


def load_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.readlines()


def replace_placeholder(html_file, placeholder="__REPLACE_ANIMALS_INFO__"):
    """ Replaces the placeholder with the animal information """
    output_lines = []
    for line in html_file:
        if placeholder in line:
            output_lines.append(serialize_animal(animal_data=load_data("animals_data.json")))
        else:
            output_lines.append(line)
    return output_lines


def write_new_html(file_path, lines):
    """ Writes the new HTML file """
    with open(file_path, "w") as handle:
        handle.writelines(lines)


def serialize_animal(animal_data):
    """ Prints the animals in the JSON file """
    output = ''
    for animal in animal_data:
        try:
            output += f'<li class="cards__item">\n'
            output += f'<div class="card__title">{animal['name']}</div>\n'
            output += f'<p class="card__text">\n'
            output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
            output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
            output += '</li>\n'
        except KeyError:
            continue
    return output

html_lines = load_html("animals_template.html")
html_lines = replace_placeholder(html_lines)
write_new_html("animals.html", html_lines)

print("HTML-File got generated.")