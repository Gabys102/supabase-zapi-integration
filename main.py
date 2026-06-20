from supabase import create_client
from dotenv import load_dotenv
import os
import requests


#variaveis do .env
load_dotenv()

#pega o s valores do .env
url = os.getenv ("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")


#conecta zapi
zapi_instance = os.getenv("ZAPI_INSTANCE")
zapi_token = os.getenv("ZAPI_TOKEN")

#validar tudo
if not url:
    raise ValueError ("SUPABASE_URL não encontrada.")
if not key:
    raise ValueError("SUPABASE_KEY não encontrada.")

if not zapi_instance:
    raise ValueError("ZAPI_INSTANCE não encontrada.")

if not zapi_token:
    raise ValueError("ZAPI_TOKEN não encontrado.")

#verificar o supabase
try:
    supabase= create_client(url,key)
except Exception as e:
    raise ValueError(f"Erro ao conectar ao Supabase: {e}")


#busca contatos
response = supabase.table("contatos").select("*").execute()

# exibe os contatos
for contato in response.data[:3]:
    print(contato["nome"], "-",contato["telefone"])
    mensagem = f"Olá, {contato['nome']} tudo bem com você?"

    print(f"Telefone: {contato['telefone']}")
    print("-" * 30)

    url_zapi = (
        f"https://api.z-api.io/instances/"
        f"{zapi_instance}/token/{zapi_token}/send-text"
    )

    payload = {
        "phone": contato["telefone"],
        "message": mensagem
    }

    response_zapi = requests.post(
        url_zapi,
        json=payload
    )

    if response_zapi.status_code == 200:
        print(f"✅ Mensagem enviada para {contato['nome']}")
    else:
        print(f"❌ Erro ao enviar para {contato['nome']}")
        print(response_zapi.status_code)
        print(response_zapi.text)
   