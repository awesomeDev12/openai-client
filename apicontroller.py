""" Open AI Api"""

import openai
from apikey import OPENAI_API_KEY
from storage_query_settings import StorageQuerySettings

openai.api_key = OPENAI_API_KEY

class APIController:
    def __init__(self):
        print("API controller constructor called")

    # Get response using the api
    def get_response_string(self,prompt_string):
        if len(prompt_string) < 6:
            return {"status":False, "text": "Invalid Input : Prompt is too small"}

        storage_query_settings = StorageQuerySettings()
        settings_dic = storage_query_settings.get_settings()
        print("Query Settings : ",settings_dic)
        # print(self.response.choices[0].text)
        response = openai.Completion.create(model=settings_dic["model"], prompt=prompt_string, temperature=settings_dic["temperature"], max_tokens=settings_dic["max_tokens"])
        output_dic = {"status":True, "text" : response.choices[0].text}
        # return response.choices[0].text
        return output_dic


# list engines
# engines = openai.Engine.list()

# print the first engine's id
# print(engines.data[0].id)

# create a completion
# completion = openai.Completion.create(engine="ada",prompt=my_prompt)
# response = openai.Completion.create(model="text-davinci-003", prompt=my_prompt, temperature=0, max_tokens=7)
