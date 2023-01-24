import json
import os
import datetime
class StorageHistory:
    def __init__(self):
        self.filename = "/home/darklord/Desktop/openai-client/history_log.json"

    def get_history(self):
        # If file does not exist then create an empty file
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
        # If file is empty then return empty list
        if os.stat(self.filename).st_size == 0:
            return []
        with open(self.filename,"r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

    def insert(self,input_string,output_string):

        # using now() to get current time
        # current_time = datetime.datetime.now()
        current_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        new_data = {"input": input_string, "output": output_string, "datetime":current_time}
        history_list = self.get_history()
        history_list.append(new_data)
        # Serializing json
        # json_object = json.dumps(history_list, indent=4)
        json_object = json.dumps(history_list)

        # Writing to history_log.json
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)

    def clear_history(self):

        history_list = []
        # Serializing json
        # json_object = json.dumps(history_list, indent=4)
        json_object = json.dumps(history_list)

        # Writing to history.json
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)
