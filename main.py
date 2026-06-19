from supabase import create_client
from dotenv import load_dotenv
import os
import requests


#variaveis do .env
load_dotenv()

#pega o s valores do .env
url = os.getenv ("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

#conecta ao supabase
supabase = create_client(url, key)

#conecta zapi
zapi_instance = os.getenv("ZAPI_INSTANCE")
zapi_token = os.getenv("ZAPI_TOKEN")

#busca contatos
response = supabase.table("contatos").select("*").execute()

# exibe os contatos
for contato in response.data:
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

   