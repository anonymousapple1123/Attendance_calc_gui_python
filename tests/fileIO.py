import json
import os

def save_settings(settings, directory = 'data',filename = 'settings.json'):
    
    os.makedirs(directory, exist_ok=True)
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..',directory, filename)
    file_path = os.path.abspath(file_path)

    with open(file_path,'w') as json_file :
        json.dump(settings,json_file, indent = 4)

def load_settings(directory = 'data', filename = 'settings.json'):
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..',directory, filename)
    file_path = os.path.abspath(file_path)

    if os.path.exists(file_path):
        with open(filename,'r') as json_file:
            return json.load(json_file)
    else:
        return {}
        #If the the file is deleted or missing make sure to create settings json file again with default values
        # I will do this later once the code is working fine with my main code.

user_settings = {
        'lecture_count_per_day' : 8,
        'fine_per_percent' : 4000,
}

save_settings(user_settings)

loaded_settings = load_settings()
print(loaded_settings)