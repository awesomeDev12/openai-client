""" Prompt """
# MyPrompt to be passed to OPEN AI

class QueryTextSettings:
    def __init__(self,model,temperature,max_tokens):
        self.model=model
        self.temperature=temperature
        self.max_tokens=max_tokens

    def get_settings(self):
        return {"model":self.model, "temperature": self.temperature, "max_tokens":self.max_tokens}
    def set_model(self,model):
        self.model = model
    def set_max_tokens(self,max_tokens):
        self.max_tokens = max_tokens
