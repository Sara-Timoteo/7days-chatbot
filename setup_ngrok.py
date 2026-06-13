import os
from dotenv import load_dotenv
from pyngrok import ngrok

load_dotenv()
ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))
print ("Authtoken registado com sucesso!")
