from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

MODELO ="llama3.2:3b"
SISTEMA = (
    "És um assistente simpático e prestável."
    "Responde de forma simples, curta e natural, em português europeu."
)

llm = ChatOllama (model=MODELO)

prompt = ChatPromptTemplate.from_messages([
    ("system", SISTEMA),
    MessagesPlaceholder(variable_name ="history"),
    ("human", "{input}"),
    ])
    
