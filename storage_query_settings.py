import json
import os


class StorageQuerySettings:
    def __init__(self):
        # dirname = os.path.dirname(__file__)
        # filename = os.path.join(dirname, 'relative/path/to/file/you/want')

        dirname = os.path.dirname(__file__)
        self.filename_text = os.path.join(dirname, 'query_text_settings.json')
        self.filename_image = os.path.join(dirname, 'query_image_settings.json')
        # self.filename_text = "/home/darklord/Desktop/openai-client/query_text_settings.json"
        # self.filename_image = "/home/darklord/Desktop/openai-client/query_image_settings.json"


    # Text settings
    # This will provide the default configuration
    def get_text_defaults(self):
        default_query_text_settings = {
            "model": "text-davinci-003",
            "temperature": 0,
            "max_tokens": 500
        }

        return default_query_text_settings

    # Function takes a dictionary as input and stores it in the file
    def set_text_settings(self, new_settings):
        # Extract info from argument
        # print("New Settings", new_settings)
        new_settings_modified = {
            "model": new_settings["model"],
            "temperature": new_settings["temperature"],
            "max_tokens": new_settings["max_tokens"]
        }
        # If File does not exist create and empty file
        if not os.path.exists(self.filename_text):
            open(self.filename_text, 'w').close()
        # Serializing json
        # json_object = json.dumps(self.history_list, indent=4)
        json_object = json.dumps(new_settings_modified)

        # Writing to query_settings.json
        with open(self.filename_text, "w") as outfile:
            outfile.write(json_object)

    # Gets current config settings from the file
    def get_text_settings(self):

        # If the file does not exist then create the file
        if not os.path.exists(self.filename_text):
            open(self.filename_text, 'w').close()

        # if the file is empty, put default settings in the file
        if os.stat(self.filename_text).st_size == 0:
            self.set_text_settings(self.get_text_defaults())

        # The file contains the current settings (default/modified)
        with open(self.filename_text, "r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

    def reset_to_text_defaults(self):
        self.set_text_settings(self.get_text_defaults())


    # Image settings

    # This will provide the default configuration
    def get_image_defaults(self):
        default_query_image_settings = {
            "model": "image-davinci-003",
            "temperature": 0,
            "max_tokens": 500
        }

        return default_query_image_settings

        # Function takes a dictionary as input and stores it in the file

    def set_image_settings(self, new_settings):
        # Extract info from argument
        # print("New Settings", new_settings)
        new_settings_modified = {
            "model": new_settings["model"],
            "temperature": new_settings["temperature"],
            "max_tokens": new_settings["max_tokens"]
        }
        # If File does not exist create and empty file
        if not os.path.exists(self.filename_image):
            open(self.filename_image, 'w').close()
        # Serializing json
        # json_object = json.dumps(self.history_list, indent=4)
        json_object = json.dumps(new_settings_modified)

        # Writing to query_settings.json
        with open(self.filename_image, "w") as outfile:
            outfile.write(json_object)

        # Gets current config settings from the file

    def get_image_settings(self):

        # If the file does not exist then create the file
        if not os.path.exists(self.filename_image):
            open(self.filename_image, 'w').close()

        # if the file is empty, put default settings in the file
        if os.stat(self.filename_image).st_size == 0:
            self.set_image_settings(self.get_image_defaults())

        # The file contains the current settings (default/modified)
        with open(self.filename_image, "r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

    def reset_to_image_defaults(self):
        self.set_image_settings(self.get_image_defaults())
