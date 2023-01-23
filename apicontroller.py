""" Open AI Api"""

import openai
from apikey import OPENAI_API_KEY
from querytextsettings import QueryTextSettings

openai.api_key = OPENAI_API_KEY

class APIController:
    def __init__(self):
        self.query_text_settings = QueryTextSettings(model="curie",temperature=0,max_tokens=60)
        self.query_text_settings.set_model("text-davinci-003")
        self.query_text_settings.set_max_tokens(500)

        print(self.query_text_settings.get_settings())

    # Get response usingthe api
    def get_response_string(self,prompt_string):
        if len(prompt_string) < 6:
            return {"status":False, "text": "Invalid Input : Prompt is too small"}

        # print(self.response.choices[0].text)
        response = openai.Completion.create(model=self.query_text_settings.model, prompt=prompt_string, temperature=self.query_text_settings.temperature, max_tokens=self.query_text_settings.max_tokens)
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
