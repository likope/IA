import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

class GeminiLlm:
    def __init__(self, model: str = "gemini-2.5-flash", temperature: float = 0.6):
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=temperature,
        )
        self.prompt = PromptTemplate.from_template("user_input: {input}")
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def invoke(self, user_input: str) -> str:
        return self.chain.invoke({"input": user_input})