from langchain_ollama import ChatOllama
llm = ChatOllama (model="llama3.2:3b")
resposta = llm.invoke ("Diz ola em portugues europeu e identifica-te numa frase.")
print (resposta.content)
