import json
import os

class StorageQuerySettings:
    def __init__(self):
        self.filename = "/home/darklord/Desktop/openai-client/query_settings.json"

    # This will provide the default configuration
    def get_defaults(self):
        default_query_settings = {
            "model" : "text-davinci-003",
            "temperature" : 0,
            "max_tokens" : 500
        }

        return default_query_settings

    # Function takes a dictionary as input and stores it in the file
    def set_settings(self,new_settings):
        # Extract info from argument
        # print("New Settings", new_settings)
        new_settings_modified = {
            "model": new_settings["model"],
            "temperature": new_settings["temperature"],
            "max_tokens": new_settings["max_tokens"]
        }
        # If File does not exist create and empty file
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
        # Serializing json
        # json_object = json.dumps(self.history_list, indent=4)
        json_object = json.dumps(new_settings_modified)

        # Writing to query_settings.json
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)

    # Gets current config settings from the file
    def get_settings(self):

        # If the file does not exist then create the file
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

        # if the file is empty, put default settings in the file
        if os.stat(self.filename).st_size == 0:
            self.set_settings(self.get_defaults())

        # The file contains the current settings (default/modified)
        with open(self.filename, "r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

    def reset_to_defaults(self):
        self.set_settings(self.get_defaults())