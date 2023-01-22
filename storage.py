import json
import os
class Storage:
    def __init__(self):
        self.history_list = self.read()

    def read(self):

        filename = "/home/darklord/Desktop/openai-client/history_log.json"
        if not os.path.exists(filename):
            open(filename, 'w').close()

        if os.stat("/home/darklord/Desktop/openai-client/history_log.json").st_size == 0:
            return []
        with open("/home/darklord/Desktop/openai-client/history_log.json","r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

        # with open('fcc.json', 'r') as fcc_file:
        #     fcc_data = json.load(fcc_file)
        #     print(fcc_data)


        print(type(f_data))

    def insert(self,input_string,output_string):
        new_data = {"input": input_string, "output": output_string}
        self.history_list.append(new_data)
        # Serializing json
        # json_object = json.dumps(self.history_list, indent=4)
        json_object = json.dumps(self.history_list)

        # Writing to history.json
        with open("/home/darklord/Desktop/openai-client/history_log.json", "w") as outfile:
            outfile.write(json_object)

