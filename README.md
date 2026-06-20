# Supabase Z-API Integration

Projeto desenvolvido em Python para integração entre Supabase e Z-API, realizando a leitura de contatos armazenados em banco de dados e o envio automatizado de mensagens personalizadas via WhatsApp.

---

## Estrutura da tabela

Tabela: `contatos`

| Campo     | Tipo        |
| --------- | ----------- |
| id        | int8        |
| criado_em | timestamptz |
| nome      | text        |
| telefone  | text        |

### Exemplo de registro

| nome | telefone      |
| ---- | ------------- |
| João | 5511988889999 |

---

## Variáveis de ambiente (.env)

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase

ZAPI_INSTANCE=sua_instancia_zapi
ZAPI_TOKEN=seu_token_zapi
ZAPI_CLIENT_TOKEN=seu_token-cliente_zapi
```

---

## Instalação

Instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## Como executar

Executar o projeto:

```bash
python main.py
```

---

## Fluxo da aplicação

1. Consulta os contatos cadastrados no Supabase.
2. Recupera os dados da tabela `contatos`.
3. Personaliza a mensagem com o nome do contato.
4. Envia a mensagem via WhatsApp utilizando a Z-API.
5. Exibe o status do envio no terminal.

---

## Demonstração

### Estrutura da tabela


<img width="1422" height="700" alt="image" src="https://github.com/user-attachments/assets/80c2c6ec-cff0-4694-8690-8d3dbb01749e" />


### Execução do projeto


<img width="575" height="236" alt="image" src="https://github.com/user-attachments/assets/e108ae8b-2309-4c55-ad58-ba633b9ffd13" />


### Mensagem recebida no WhatsApp


<img width="327" height="800" alt="image" src="https://github.com/user-attachments/assets/458ab461-51da-43e2-b131-983fd34fad2f" />


---

## Tecnologias utilizadas

* Python
* Supabase
* Z-API
* Requests
* Python Dotenv

---

## Autor

Gabrielle Batista da Costa
