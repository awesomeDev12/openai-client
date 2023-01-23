import json
import os
import datetime
class Storage:
    def __init__(self):
        self.filename = "/home/darklord/Desktop/openai-client/history_log.json"
        self.history_list = self.read()

    def read(self):

        # filename = "/home/darklord/Desktop/openai-client/history_log.json"
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

        if os.stat(self.filename).st_size == 0:
            return []
        with open(self.filename,"r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

        # with open('fcc.json', 'r') as fcc_file:
        #     fcc_data = json.load(fcc_file)
        #     print(fcc_data)


        # print(type(f_data))

    def insert(self,input_string,output_string):

        # using now() to get current time
        # current_time = datetime.datetime.now()
        current_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        new_data = {"input": input_string, "output": output_string, "datetime":current_time}
        self.history_list.append(new_data)
        # Serializing json
        # json_object = json.dumps(self.history_list, indent=4)
        json_object = json.dumps(self.history_list)

        # Writing to history.json
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)

    def get_history(self):

        # this is not the history_list of class this is a local variable

        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

        if os.stat(self.filename).st_size == 0:
            return []
        with open(self.filename, "r") as f:
            f_data = json.load(f)
        # print(f_data)
        return f_data

