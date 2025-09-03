import json
import data_fetcher


def load_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.readlines()


def replace_placeholder(html_file, placeholder="__REPLACE_ANIMALS_INFO__"):
    """ Replaces the placeholder with the animal information """
    output_lines = []

    searched_name = input("Enter a name of an animal: ").strip()
    animal_data = data_fetcher.fetch_data(searched_name)

    for line in html_file:
        if placeholder in line:
            output_lines.append(serialize_animal(animal_data, searched_name))
        else:
            output_lines.append(line)
    return output_lines


def write_new_html(file_path, lines):
    """ Writes the new HTML file """
    with open(file_path, "w") as handle:
        handle.writelines(lines)


def serialize_animal(animal_data, searched_name):
    """ Prints the animals in the HTML file or message if not found """
    if not animal_data:
        return f"<h2>The animal '{searched_name}' doesn't exist.</h2>"

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