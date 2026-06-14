from app import conversa

cfg = {"configurable": {"session_id": "teste"}}
print(conversa.invoke({"input": "O meu nome é Sara."}, config=cfg).content)
print(conversa.invoke({"input": "Qual é o meu nome?"}, config=cfg).content)
