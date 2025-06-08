import json
import os
read_validation = False #both not used currently
write_validation = False

def save_settings(settings, directory = 'data',filename = 'settings.json'):
    
    os.makedirs(directory, exist_ok=True)
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..',directory, filename)
    file_path = os.path.abspath(file_path)

    with open(file_path,'w') as json_file :
        json.dump(settings,json_file, indent = 4)
        write_validation = True

def load_settings(directory = 'data', filename = 'settings.json'):
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..',directory, filename)
    file_path = os.path.abspath(file_path)

    if os.path.exists(file_path):
        with open(file_path,'r') as json_file:
            return json.load(json_file)
        read_validation = True
        
    else:
        return {}
        #If the the file is deleted or missing make sure to create settings json file again with default values
        # I will do this later once the code is working fine with my main code.
