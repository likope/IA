#Import
from langchain_core.runnables import RunnableLambda, RunnableAssign, StrOutputParser
from langchain_ollama import ChatOllama


#definisco un input generico di test
test_input = "Hello, who are you?"

#definisco l'url del server Ollama
ollama_url = "http://localhost:11434"

#definisco il modello di chat
model_llm = "assistente"

#definisco la dict state che conterrà i parametri della conversazione
state = {
    "input" : test_input,
    "output": "",
    "history": ""
}


#definisco i parametri del modello di chat su ollama
llm = ChatOllama(
    model = model_llm,
    temperature = 0.5,
    base_url = ollama_url,
    )


#definisco una f che prende l input e output e costruisce la history relativa nel state
def update_history(state: dict) -> str:
    return state["history"] + f"User input: {state['input']}, Assistant output: {state['output']}"


#determino la chain
chain = (
    RunnableAssign({"output": llm | StrOutputParser() }) | RunnableAssign({"history": update_history})
)


if __name__ == "__main__":
    #eseguo la chain
    result = chain.invoke(state)
    print(result)