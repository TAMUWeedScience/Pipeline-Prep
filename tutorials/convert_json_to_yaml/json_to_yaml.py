#.json to .yaml

import yaml
import json

#function to convert .json file to .yaml
def json_to_yaml(file_path, output_file_name):

    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    with open(output_file_name, "w") as yaml_file:
        yaml.dump(json_data, yaml_file)

json_to_yaml("exif_data.json", "exif_data.yaml")

