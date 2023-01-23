""" Prompt """
# MyPrompt to be passed to OPEN AI

class QueryTextSettings:
    def __init__(self,model="text-davinci-003",temperature=0,max_tokens=60):
        self.model=model
        self.temperature=temperature
        self.max_tokens=max_tokens

    def set_max_tokens(self,max_tokens):
        self.max_tokens = max_tokens
