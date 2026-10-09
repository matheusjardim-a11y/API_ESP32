import requests

API_link = "http://10.161.161.220/api/dados"

resposta = requests.get(API_link)

code = resposta.status_code

if code == 200:
    dados = resposta.json()
    print("Busca concluida.")
    temperatura = dados["temperatura"], 
    umidade = dados["umidade"]
    print(f"Temperatura:{temperatura}")
    print(f"Umidade:{umidade}")
    
elif code >= 400:
    response_erro = resposta.json()
    codigo = response_erro['code']
    mensagem = response_erro['message']

    print(f"Código do erro: {codigo} ")
    print(f"Motivo do erro: {mensagem}")
else:
    print("Deu preguiça de procurar, mas acho que o que você quer tá em outro lugar ;)")