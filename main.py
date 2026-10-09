import requests
from pprint import pprint

API_link = ""

params = {
    
}

response = requests.get(API_link, params=params)

code = response.status_code

if code == 200:
    dados = response.json()
    print("Busca concluida.")
    
elif code >= 400:
    response_erro = response.json()
    codigo = response_erro['code']
    mensagem = response_erro['message']

    print(f"Código do erro: {codigo} ")
    print(f"Motivo do erro: {mensagem}")
else:
    print("Deu preguiça de procurar, mas acho que o que você quer tá em outro lugar ;)")