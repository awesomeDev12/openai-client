import json

class Storage:
    def __init__(self):
        self.history_list = []

    def read(self):
        with open("history_log.json") as f:
            data = json.load(f)
        print(data)
        print(type(data))

    def insert(self,input_string,output_string):
        new_data = {"input": input_string, "output": output_string}
        self.history_list.append(new_data)
        # Serializing json
        json_object = json.dumps(self.history_list, indent=4)
        # Writing to history.json
        with open("history_log.json", "w") as outfile:
            outfile.write(json_object)

