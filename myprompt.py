""" Prompt """
# MyPrompt to be passed to OPEN AI

class MyPrompt:
    def __init__(self, prompt_string, model="text-davinci-003",temperature=0,max_tokens=60):
        self.prompt_string=prompt_string
        self.model=model
        self.temperature=temperature
        self.max_tokens=max_tokens

    def get_prompt_string(self):
        return self.prompt_string

    def set_prompt_string(self,prompt_string):
        self.prompt_string = prompt_string

    def set_max_tokens(self,max_tokens):
        self.max_tokens = max_tokens
