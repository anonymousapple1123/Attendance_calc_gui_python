import json
import os
import sys

read_validation = False
write_validation = False

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS  # Only exists in PyInstaller bundles
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_settings_path(directory='data', filename='settings.json'):
    # Store settings next to the executable or in current working directory
    dir_path = resource_path(directory)
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(dir_path, filename)

def save_settings(settings, directory='data', filename='settings.json'):
    global write_validation
    file_path = get_settings_path(directory, filename)
    with open(file_path, 'w') as json_file:
        json.dump(settings, json_file, indent=4)
        write_validation = True

def load_settings(directory='data', filename='settings.json'):
    global read_validation
    file_path = get_settings_path(directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            read_validation = True
            return json.load(json_file)
    else:
        return {}
