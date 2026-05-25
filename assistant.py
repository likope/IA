"""
File che gestisce l'assistente, il prompt e il metodo di generazione.
"""

from client import GeminiLlm
from langchain_core.prompts import PromptTemplate

class Assistant:
    def __init__ (self, user_input: str):
        self.state = {"input": user_input,
                      "history": ""}
        self.gemini = GeminiLlm()
        self.template = """Sei un llm, il tuo compito è quello di rispondere nel modo migliore e piu coerente possibile dato il user input e la storia della conversazione. 
        user_input = {input}, 
        storia_della_conversazione = {history}."""
        self.prompt = PromptTemplate.from_template(self.template)
        self.chain = self.prompt | self.gemini.generate

    def Ask (self): 
        self.risposta = self.chain.invoke(self.state)
        return self.risposta