import requests
from pprint import pprint

API_link = "http://10.161.161.220/api/dados"

def buscar_dados():

    try:
        response = requests.get(API_link, timeout=5)
        response.raise_for_status()

        dados = response.json()

        print("Dados recebidos com sucesso")
        pprint(dados)

        temperatura = dados.get("temperatura")
        umidade =  dados.get("umidade")

        if temperatura is not None:
            print(f"A temperatura é: {temperatura}°C")

        if umidade is not None:
            print(f"A umidade é: {umidade}%")

    except requests.exceptions.Timeout:
        print("Erro: o ESP32 demorou para responder.")

    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao ESP32.")

    except requests.exceptions.HTTPError as erro:
        print(f"Erro HTTP: {erro}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")

    except ValueError:
        print("Erro: a resposta não contém um JSON válido.")

buscar_dados()