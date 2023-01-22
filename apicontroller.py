""" Open AI Api"""

import openai
from apikey import OPENAI_API_KEY
from myprompt import MyPrompt

openai.api_key = OPENAI_API_KEY

class APIController:
    def __init__(self,prompt_string=""):
        self.my_prompt = MyPrompt(prompt_string="")
        self.my_prompt.set_max_tokens(499)
        self.my_prompt.set_prompt_string(prompt_string)


    def set_prompt_string(self,prompt_string):
        self.my_prompt.set_prompt_string(prompt_string)
    # print the response
    def get_response_string(self):
        # print(self.response.choices[0].text)
        response = openai.Completion.create(model=self.my_prompt.model, prompt=self.my_prompt.prompt_string, temperature=self.my_prompt.temperature, max_tokens=self.my_prompt.max_tokens)
        return response.choices[0].text


# list engines
# engines = openai.Engine.list()

# print the first engine's id
# print(engines.data[0].id)

# create a completion
# completion = openai.Completion.create(engine="ada",prompt=my_prompt)
# response = openai.Completion.create(model="text-davinci-003", prompt=my_prompt, temperature=0, max_tokens=7)
