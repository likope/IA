"""
File che contiene e gestisce il client del progetto, qui vengono gestiti i parametri e viene definita la chiamata del modello.
"""


import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

class GeminiLlm:
    """Classe che determina i parametri del modello di llm e che definisce l'effettuazione delle chiamate."""

    #Inizializzazione e specifiche dei parametri:

    def __init__(self, model: str = "gemini-2.5-flash", temperature: float = 0.8):
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=temperature,
        )

    #Metodo che effettua la chiamata prendendo un prompt

    def generate(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content