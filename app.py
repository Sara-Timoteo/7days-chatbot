import uuid
import chainlit as cl
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

MODELO = "llama3.2:3b"
SISTEMA = (
    "És um assistente simpático e prestável. "
    "Responde de forma simples, curta e natural, em português europeu."
)

llm = ChatOllama(model=MODELO)

prompt = ChatPromptTemplate.from_messages([
    ("system", SISTEMA),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

cadeia = prompt | llm

_historicos = {}

def obter_historico(session_id: str):
    if session_id not in _historicos:
        _historicos[session_id] = InMemoryChatMessageHistory()
    return _historicos[session_id]

conversa = RunnableWithMessageHistory(
    cadeia,
    obter_historico,
    input_messages_key="input",
    history_messages_key="history",
)


@cl.on_chat_start
async def responder (mensagem: cl.Message):
    session_id = cl.user_session.get("session_id")
    resposta = cl.Message(content="")
    async for parte in conversa.astream(
        {"input": mensagem.content},
        config={"configurable": {"session:id": session_id}},
    ) :

        await resposta.stream_token(parte.content)
    await resposta.send()
