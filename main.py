from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


dict = {
    "input": "chi sei?",
    "output": "",
    "history": "",
    "first_response": "",
    "second_response": ""
}

template = """Sei un assistente, rispondi nel modo più coerente possibile all'input dell'utente (user_input) tenendo conto anche della cronologia della conversazione (history).
user_input: {input},
history: {history}"""
prompt = PromptTemplate.from_template(template, template_format="f-string")

llm = ChatOllama(
    model = "assistente",
    temperature = 0.6,
    base_url = "http://localhost:11434"
)

chain = prompt|llm|StrOutputParser


if __name__ == "__main__":
    response = chain.invoke(dict)
    print(response)