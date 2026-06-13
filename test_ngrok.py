import os
from dotenv import load_dotenv
from pyngrok import ngrok

load_dotenv()
ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))

tunel = ngrok.connect("8000")
print ("URL publico: ", tunel.public_url)
input ("Carregue em Enter para fechar o tunel...")
ngrok.disconnect(tunel.public_url)
